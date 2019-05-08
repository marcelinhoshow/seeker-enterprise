import pymongo
import csv

conexao = pymongo.MongoClient('mongodb+srv://botpython:bc123456!@storm-project-eu6jj.mongodb.net/SeekerEnterprise')
mydb = conexao['SeekerEnterprise']

def gerarRelatorio(nomeEmpresa):
	novoArquivo = open('relatorioSaida.csv','+a')

	busca = mydb.dadosEmpresas.find_one({
		'nomeEmpresa' : nomeEmpresa
	})

	telefoneEmpresa = busca['telefoneEmpresa']

	novoArquivo.write(nomeEmpresa+';'+telefoneEmpresa+'\n')

gerarRelatorio('Coca Cola')
