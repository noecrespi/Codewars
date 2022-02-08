""" 
https://www.codewars.com/kata/57f781872e3d8ca2a000007e

Dada una matriz (lista) de enteros, devuelve una nueva
matriz (lista) con cada uno de sus valores duplicado.

Por ejemplo:

[1, 2, 3] --> [2, 4, 6]
"""

def maps(matriz):
    newlit = []
    for number in matriz:
        resultado = number * 2
        #append = insertar (añadir) al final de la lista
        newlit.append(resultado)
    return newlit
