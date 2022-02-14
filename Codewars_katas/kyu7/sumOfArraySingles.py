"""
https://www.codewars.com/kata/59f11118a5e129e591000134

En este Kata, se le dará una serie de números en los que dos números aparecen una vez y el resto sólo dos veces. Su tarea será devolver la suma de los números que ocurren solo una vez.

Por ejemplo, repeats([4,5,7,5,4,8]) = 15porque solo los números 7y 8ocurren una vez, y su suma es 15. Cada otro número ocurre dos veces.

Problema:
    sumar los numeros NO repetidos de una lista

Algoritmo:
    ir numero por numero de la lista
        contar cuantas veces sale el numero en la lista
        si solo sale una vez, sumo el numero al resultado
    devuelvo el resultado
"""

#definimos una funcion llamada reapeats que recoge el argumento <lista 'list'>
def repeats(lista):
    resultado = 0
    #para cada numero de la lista 
    for numero in lista:
        #si el NUMERO DE VECES QUE SE ENCUENTRA LO QUE SEA EN EL CONJUNTO es igual a 1
        if lista.count(numero) == 1:
            resultado += numero
    return resultado
