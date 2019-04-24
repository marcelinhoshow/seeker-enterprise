from googlesearch import search
import requests
from bs4 import BeautifulSoup
import csv
import re

# Algorithm By Seeker Enterprise! All Rights Reserved! Open Source 4ever. Like and Follow Project
# in GitLab - https://gitlab.com/BDAg/stormproject/seeker-enterprise

class Seeker():

	def __init__(self): #Function By Jorge
		fileName = str(input('-> INSIRA O NOME DO ARQUIVO CSV : '))
		self.getNamesEnterprises(fileName)

	def getNamesEnterprises(self,nomeArquivo): #Function By Ana Flavia, Nathalia
		with open(str(nomeArquivo)+'.csv', 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				nomeEmpresa = row[0]
				sitesList = self.getSitesEnterprises(str(nomeEmpresa))

	def getSitesEnterprises(self,nomeEmpresa): #Function By Ana Flavia, Nathalia
		listaSites = []
		for url in search(nomeEmpresa, stop=10):
			listaSites.append(url)
		return listaSites
		
Seeker()