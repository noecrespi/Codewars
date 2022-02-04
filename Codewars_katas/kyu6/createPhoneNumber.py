""" 
https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

Escriba una función que acepte una matriz de 10 enteros (entre 0 y 9), que devuelva una cadena de esos números en forma de número de teléfono.

Ejemplo
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
El formato devuelto debe ser correcto para completar este desafío.
¡No olvides el espacio después de los paréntesis de cierre!
"""

def create_phone_number(n: list):
    numeros = []
    for num in n:
        numeros.append(str(num))

    parte1 = numeros[0:3]
    parte2 = numeros[3:6]
    parte3 = numeros[6:10]
    
    return  "(" + "".join(parte1) + ") " + "".join(parte2) + "-" + "".join(parte3)

if __name__ == '__main__':
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
