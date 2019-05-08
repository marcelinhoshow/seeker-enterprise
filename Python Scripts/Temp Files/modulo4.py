from googlesearch import search
from bs4 import BeautifulSoup
import csv
import requests

vetorLinksSecundarios = []
visitados = []

def reqLinksPrimario(linksPrimarios):
    req = requests.get(linksPrimarios)
    print ('Primario : '+str(linksPrimarios)+'\n')
    getLinks(req,linksPrimarios)

def reqLinksSecundario(linksSecundarios):
    print ('Secundario : '+str(linksSecundarios))
    try:
        req = requests.get(linksSecundarios)
        getLinks(req,linksSecundarios)
    except:
        pass

def getLinks(requisicao,linkPrimario):
    soupInterno = BeautifulSoup(requisicao.content,'html.parser')
    allLinksInterno = soupInterno.find_all('a')
    
    for linksSecundarios in allLinksInterno:
        try:
            filtro = (linksSecundarios['href'])
            if 'facebook' in filtro or 'instagram' in filtro or 'twitter' in filtro or 'youtube' in filtro:
                pass
            else:
                if filtro[0] == '/' or filtro[0] == '#':
                    linksSecundario = linkPrimario+filtro
                else:
                    linksSecundario = filtro

                if not linksSecundario in visitados:
                    
                    if len(vetorLinksSecundarios) < 10:
                        vetorLinksSecundarios.append(linksSecundario)
                        visitados.append(linksSecundario)
        except:
            pass

    linksSecundario = vetorLinksSecundarios[0]
    vetorLinksSecundarios.pop(0)
    reqLinksSecundario(linksSecundario)

def getByName(nomeEmpresa):
    listaSites = []
    for url in search(nomeEmpresa, stop=10):
        listaSites.append(url)
    return listaSites

arraySites = getByName('Coca Cola')

for linksPrimarios in arraySites:
    reqLinksPrimario(linksPrimarios)