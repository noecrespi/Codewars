"""
https://www.codewars.com/kata/57cc975ed542d3148f00015b

Se le dará una matriz ay un valor x. Todo lo que necesita hacer es verificar si la matriz proporcionada contiene el valor.

Array puede contener números o cadenas. X puede ser cualquiera.

Retorna truesi la matriz contiene el valor, falsesi no.
"""

"""
    1º si en la lista tiene el valor x 
    2º devuelve true
    3º si la lista no tine el valor x 
    5º return false 
"""

# DEFine una funcion llamada <check> que recoge los ARGUMENTOS <listaValores> y <X>
def check(listaValores, X):
    # para cada x de la listaValores
    for valor in listaValores:
        #si el valor es igual a x
        if valor == X:
            #devolver true
            return True

    return False
    