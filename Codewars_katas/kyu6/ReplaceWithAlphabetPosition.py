"""
https://www.codewars.com/kata/546f922b54af40e1e90001da

Bienvenidos.

En este kata, se requiere que, dada una cadena, reemplace cada letra con su posición en el alfabeto.

Si algo en el texto no es una carta, ignóralo y no lo devuelvas.

"a" = 1, "b" = 2, etc
"""

""" 
Convertir el texto cada una de sus letras en la posición del abecedario
    1º crear una lista de las lefras del abecedario / importar libreria
    2º tendremos que iterar las letras de un texto 
    3º buscar en que posición está en el abecedario
    4º guardar la posición quen un string a devover
    5º devolver el string
"""

import string

def alphabet_position(text):
    nuevotexto = ''
    text = text.lower()
    for letra in text:
        if letra.isalpha() == True:
            posicion = string.ascii_lowercase.find(letra) + 1
            nuevotexto = nuevotexto + ' ' + str(posicion)
    return nuevotexto.strip()
    