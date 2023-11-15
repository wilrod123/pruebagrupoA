

import pandas as pd

from bs4 import BeautifulSoup

import requests
#Escribe una función en Python que calcule el factorial de un número entero no negativo.
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "solo # no negativos"   
    else:
        return n * factorial(n - 1)


#Escribe una función en Python que cuente la cantidad de palabras en una cadena de texto.
def contar(texto):
    palabras = texto.split()
    return len(palabras)  

#texto = "la vida es bella"
#cantidad = contar(texto)
#print(cantidad) 


#def mostrar_primeros_registros():
url = 'https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
dataset_html = soup.find_all('span', class_='heading')
print(dataset_html)







