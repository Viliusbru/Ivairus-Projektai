import requests


def names():
    url = 'https://api.frankfurter.app/currencies'
    listas = []
    r = requests.get(url).json()
    for currency in r:
        listas.append(currency)
    return listas

def convert(skaicius, valiuta1, valiuta2):
    url_start = 'https://api.frankfurter.app/latest?amount='
    url_end = ''
    url_end = url_start + skaicius + '&from=' + valiuta1 + '&to=' + valiuta2
    r = requests.get(url_end).json()
    return r['rates']