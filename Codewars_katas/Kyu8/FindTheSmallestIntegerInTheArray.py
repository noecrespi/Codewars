""" 
https://www.codewars.com/kata/55a2d7ebe362935a210000b2

Dada una matriz de números enteros, su solución debería encontrar el número entero más pequeño.

Por ejemplo:

Dada [34, 15, 88, 2]tu solución volverá2
Dada [34, -345, -1, 100]tu solución volverá-345
Puede asumir, a los efectos de este kata, que la matriz proporcionada no estará vacía.
"""

""" 
    1º crear pila (variable) del numero más peque 
    2º iterar la lista
    3º comprovar si el num que tengo en la lista es más pequeño que el exitente 
    4º devolver el num más peque
"""

def find_smallest_int(lista):
    # 1º crear pila del numero más peque
    numpeque = lista[0]
    # iteramos la lista de núm 
    for number in lista :
        #3º comprovar si el num que tengo en la lista es más pequeño que el exitente 
        if number < numpeque: 
            numpeque = number
    #4º devolver el num más peque
    return numpeque
    