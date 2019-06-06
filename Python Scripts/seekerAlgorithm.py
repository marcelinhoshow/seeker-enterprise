from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pymongo
import csv
import re
import os

# Algorithm By Seeker Enterprise! All Rights Reserved! Open Source 4ever. Like and Follow Project
# in GitLab - https://gitlab.com/BDAg/stormproject/seeker-enterprise

class Seeker():

	def __init__(self): #Function By Jorge
		global sitesVisitados
		global sitesPendentes

		sitesVisitados = []
		sitesPendentes = []

		while True:
			fileName = str(input('-> INSIRA O NOME DO ARQUIVO CSV : '))
			if os.path.isfile(fileName+'.csv'):
				break
			else:
				print ('NOME DE ARQUIVO INVALIDO!')

		self.mydb = self.connectPymongo()
		self.getNamesEnterprises(fileName)

	def connectPymongo(self): #Function By Jorge
		self.conexao = pymongo.MongoClient('mongodb+srv://botpython:bc123456!@storm-project-eu6jj.mongodb.net/SeekerEnterprise')
		self.mydb = self.conexao['SeekerEnterprise']

		return self.mydb

	def findEmpresaInBD(self,nomeEmpresa): #Function By Jorge
		buscaMongo = self.mydb.dadosEmpresas.find_one({
			'nomeEmpresa' : nomeEmpresa
		})

		if buscaMongo != None:
			return True
		else:
			return None

	def setCabecalhoCSVSaida(self): #Function By Jorge
		novoArquivo = open('relatorioSaida.csv','+a')
		novoArquivo.write('Nome Empresa;Telefones;Confiabilidade\n\n')

	def getNamesEnterprises(self,nomeArquivo): #Function By Ana Flavia, Nathalia (First Module)
		with open(str(nomeArquivo)+'.csv', 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				nomeEmpresa = row[0]
				print('Iniciando busca por {}'.format(nomeEmpresa))
				contadorRanking = 1
				verificarEmpresaNoBanco = self.findEmpresaInBD(nomeEmpresa)
				if verificarEmpresaNoBanco == None:
					sitesList = self.getSitesEnterprises(str(nomeEmpresa))
					for sites in sitesList:
						self.requisitarLinkInicial(sites)
						if len(celPhone) != 0:
							rankingEmpresa = self.setRankingCelPhone(contadorRanking)
							self.sendToMongo(nomeEmpresa,celPhone,rankingEmpresa)
							print ('Empresa Analisada : {}\nTelefones Obtidos : {}\nConfiabilidade : {}\n'.format(nomeEmpresa,str(celPhone).replace("'","").replace("[","").replace("]",""),rankingEmpresa))
							break
						contadorRanking+=1
				else:
					print ('Empresa Analisada {}\nDados Já Existentes no Banco de Dados\n'.format(nomeEmpresa))
				
				self.getListNumbers(nomeEmpresa)

	def getSitesEnterprises(self,nomeEmpresa): #Function By Ana Flavia, Nathalia (First Module)
		listaSites = []
		for url in search(nomeEmpresa, stop=10):
			listaSites.append(url)
		return listaSites
		
	def requisitarLinkInicial(self,siteEmpresa): #Function By Ana Flavia, Nathalia (First Module)
		requisicao = requests.get(siteEmpresa)
		self.getLinkAndText(requisicao)
	
	def requisitarLinkSecundario(self,siteEmpresa): #Function By Ana Flavia, Nathalia (First Module)
		requisicao = requests.get(siteEmpresa)
		self.getLinkAndText(requisicao)

	def findCelInText(self,texto): #Function By Helena, Janaina, Gabriel, Jorge (Third Module)
		listaPhones = []
		listaExpressoes = ['(\([0-9]{2}\) [0-9]{5}-[0-9]{4})','(\([0-9]{2}\) [0-9]{5} [0-9]{4})','(\([0-9]{2}\) [0-9]{4}[0-9]{5})','(\([0-9]{2}\) [0-9]{4}[0-9]{5})','(\+[0-9]{13})','([0-9]{4} [0-9]{3} [0-9]{2} [0-9]{2})','([0-9]{4}-[0-9]{3}-[0-9]{2}-[0-9]{2})','([0-9]{4} [0-9]{3} [0-9]{4})','([0-9]{2} [0-9]{2} [0-9]{4}-[0-9]{4})','(\[0-9]{2} [0-9]{2} [0-9]{4}-[0-9]{4})','([0-9]{2} [0-9]{4} [0-9]{4})','(\([0-9]{2}\) [0-9]{4}-[0-9]{4})','(\([0-9]{2}\) [0-9]{4} [0-9]{4})','(\+[0-9]{2} \([0-9]{2}\) [0-9]{4} [0-9]{4})']
		
		for expressao in listaExpressoes:
			phones = re.findall(expressao, texto)
			if len(phones) != 0:
				for numbers in phones:
					if numbers not in listaPhones:
						listaPhones.append(numbers)
		
		if len(listaPhones) != 0:
			return listaPhones
		else:
			return []

	def getLinkAndText(self,requisicao): #Function By Ana Luísa, Marcelo, Lara, Nathalia, Ana Flávia, Jorge (Second and Fourth Module)
		global celPhone

		soupInterno = BeautifulSoup(requisicao.content,'html.parser')
		textoSite = soupInterno.text
		linksSite = soupInterno.find_all('a')

		for linksSecundarios in linksSite:
			try:
				filtro = (linksSecundarios['href'])
				if 'facebook' in filtro or 'instagram' in filtro or 'twitter' in filtro or 'youtube' in filtro or 'tel:' in filtro or 'javascript' in filtro or not 'www' in filtro or 'cocacolashoes' in filtro or 'cocacolajeans' in filtro:
					pass
				else:
					if filtro[0] == '/' or filtro[0] == '#':
						linksSecundario = linkPrimario+filtro
					else:
						linksSecundario = filtro
					sitesPendentes.append(linksSecundario)
			except:
				pass

		celPhone = self.findCelInText(textoSite)

		if celPhone != []:
			sitesPendentes.clear()

		if len(sitesPendentes) != 0:
			firstLink = sitesPendentes[0]
			sitesPendentes.pop(0)
			if firstLink not in sitesVisitados:
				sitesVisitados.append(firstLink)
				self.requisitarLinkSecundario(firstLink)

	def sendToMongo(self,nomeEmpresa,telefoneEmpresa,rankingEmpresa): #Function By Marcelo, Lara, Janaina (Fifth Module)
		buscaMongo = self.mydb.dadosEmpresas.find_one({
			'nomeEmpresa' : nomeEmpresa
		})

		if buscaMongo == None:
			self.mydb.dadosEmpresas.insert({
				'nomeEmpresa' : nomeEmpresa,
				'telefoneEmpresa' : telefoneEmpresa,
				'rankingEmpresa' : rankingEmpresa
			})

	def setRankingCelPhone(self,contadorUrl): #Function By Helena, Ana Luisa, Gabriel, Jorge (Sixth Module)

		if contadorUrl < 3:
			ranking = 'Alta Confiabilidade'

		elif contadorUrl > 3 and contadorUrl < 6:
			ranking = "Média Confiabilidade"

		else:
			ranking = 'Baixa Confiabilidade'

		return ranking

	def getListNumbers(self,nomeEmpresa): #Function By Helena, Ana Luisa, Gabriel (Sixth Module)
		novoArquivo = open('relatorioSaida.csv','+a')

		busca = self.mydb.dadosEmpresas.find_one({
			'nomeEmpresa' : nomeEmpresa
		})

		telefoneEmpresa = busca['telefoneEmpresa']
		rankingEmpresa = busca['rankingEmpresa']

		telefoneEmpresaTratado = str(telefoneEmpresa).replace("'","").replace("[","").replace("]","")

		novoArquivo.write(nomeEmpresa+';'+telefoneEmpresaTratado+';'+rankingEmpresa+'\n')

Seeker()