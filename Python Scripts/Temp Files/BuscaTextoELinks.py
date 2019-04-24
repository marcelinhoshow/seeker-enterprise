import requests
from bs4 import BeautifulSoup

codigo_array = []

linkTeste = 'https://www.dafiti.com.br'

def modulo1(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')

    allLinks = soup.find_all('a') 

    for linkIndividual in allLinks:
        try:
            filtro = (linkIndividual['href'])
            if 'facebook' in filtro or 'instagram' in filtro or 'twitter' in filtro or 'youtube' in filtro:
                pass
            else:
                if filtro[0] == '/' or filtro[0] == '#':
                    codigo_array.append(page+filtro)
                else:
                    codigo_array.append(filtro)
        except:
            pass
    
    return codigo_array

variavel = modulo1(linkTeste)
print (variavel)