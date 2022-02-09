""" 
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

Si enumeramos todos los números naturales debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Termina la solución para que devuelva la suma de todos los múltiplos de 3 o 5 por debajo del número pasado. Además, si el número es negativo, devuelve 0 (para los idiomas que los tienen).

Nota: si el número es un múltiplo de 3 y 5, solo cuéntelo una vez .
"""
    


def solution(number: int):

    resulMultiplos = 0
    todosMultiplos = set()
    consecutivo3 = []


    if number >=3:

        consecutivo3 = set(range(0, number, 3))
        consecutivo5 = set(range(0, number, 5))

        resulMultiplos = consecutivo3 | consecutivo5 


        return sum(resulMultiplos)

    else:
        return 0
        



if __name__ == '__main__':

    assert solution(16) == 60
    assert solution(200) == 9168
    assert solution(-1) == 0
    assert solution(6) == 8
    assert solution(4) == 3
    assert solution(3) == 0
    assert solution(5)== 3
    assert solution(15) == 45
    assert solution(0) == 0
    assert solution(10) == 23
    assert solution(20) == 78
