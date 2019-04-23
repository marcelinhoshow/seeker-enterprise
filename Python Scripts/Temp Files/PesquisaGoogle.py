from googlesearch import search
import csv

def funcaoArquivos(nomeArquivo):
    listaSites = []
    with open(str(nomeArquivo)+'.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            nomeEmpresa = row[0]
            for url in search(nomeEmpresa, stop=10):
                listaSites.append(url)
    return listaSites

arraySites = funcaoArquivos('teste')
print (arraySites)