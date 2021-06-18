import requests
from bs4 import BeautifulSoup
import random

url = 'https://www.delfi.lt/'
r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")
antrastes = soup.find_all(class_='CBarticleTitle')

tuscias_listas = []
pries = []
po = []
final_list = []
sk = 0
for antraste in antrastes:
    x = antraste.get_text()
    if ':' in x:
        tuscias_listas.append(x)

for i in tuscias_listas:
    pries.append(i.split(':')[0])
    po.append(i.split(':')[1])

# print(pries)
random.shuffle(po)
for item in pries:
    final_list.append(item + ':' + po[sk])
    sk += 1

print(*final_list, sep = "\n") 
