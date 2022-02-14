""" 
https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

Su tarea es encontrar el primer elemento 
de una matriz que no sea consecutivo.

Por no consecutivo queremos decir que no es exactamente 
1 más grande que el elemento anterior de la matriz.

Por ejemplo, si tenemos una matriz [1,2,3,4,6,7,8]a
continuación, 1a continuación, 2a continuación, 3a
continuación, 4son todos consecutivos, pero 6no lo
es, así que ese es el primer número no consecutivos.

Si toda la matriz es consecutiva, devuelve null2 .

La matriz siempre tendrá al menos los 2elementos 1 
y todos los elementos serán números. Los números
también serán todos únicos y en orden ascendente.
¡Los números pueden ser positivos o negativos y el
primer no consecutivo también puede serlo!


problema: hay que comprovar lista de num es consecutiva

    1. coger todos los num
    2. mirar los num (iterar)
    3. seleccionaremos el segundo y le restaremos 1 
    4. el resultado que de tiene que ser el mismo que el num anterior al    seleccionado 
    5. si no lo es no son num consecutivos
"""



def first_non_consecutive(lista):
    posicion = 0 
    for number in lista:
        #la 'lista' empieza desde la posición 0 pero 'len' empieza a contar desde 1
        if len(lista)-1 != posicion and (number != lista[posicion + 1]-1):
            return lista[posicion + 1]
        posicion = posicion + 1
        