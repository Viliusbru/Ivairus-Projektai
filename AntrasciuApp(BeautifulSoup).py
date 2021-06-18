import requests
from bs4 import BeautifulSoup
citatos = []
autoriai = []
url = 'http://quotes.toscrape.com/'

r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
def citatos_traukimas():
    find = soup.find_all(class_='text')
    for quote in find:
        x = quote.get_text()
        citatos.append(x)
    return citatos
citatos_traukimas()

def vardo_traukimas():
    find = soup.find_all(class_='quote')
    for quote in find:
        x = quote.get_text().split('by')[1]
        autoriai.append(x)
        return autoriai

citatos_traukimas()
vardo_traukimas()
print(autoriai)