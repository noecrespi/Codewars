"""
https://www.codewars.com/kata/61ce25e92ca4fb000f689fb0

ISBN significa International Standard Book Number.

Durante más de treinta años, los ISBN tenían 10 dígitos. El 1 de enero de 2007, el sistema ISBN cambió a un formato de 13 dígitos. Ahora todos los ISBN tienen 13 dígitos. En realidad, no hay una gran diferencia entre ellos. Puede convertir un ISBN de 10 dígitos en un ISBN de 13 dígitos agregando el número de prefijo (978) al principio y luego volviendo a calcular el último dígito de verificación usando un método bastante simple.

Método
1. Tome el ISBN ("1-85326-158-0") .
2. Elimina el último carácter, que puede ser un número o "X".
3. Agregue el número de prefijo (978) y un guión (-) al principio.
4.Tome los 12 dígitos, luego multiplique alternativamente cada dígito de izquierda a derecha por 1 o 3.
5. Suma los 12 números que obtuviste.
6. Tome el número y realice una división módulo 10.
7. Si el resultado es 0, el dígito de control es 0. Si no es 0, resta el resultado de 10. En este caso, ese es el dígito de control.
8. Agregue el dígito de control al final del resultado del paso 3.
9. Devuelva el ISBN de 13 dígitos en el formato adecuado:
" prefix number- original ISBN except the last character- check digit"
" 978- 1- 85326- 158- 9"
"""

def isbn_converter(isbn):

    menosCaracacter = isbn[:-1]
    masPrefijo = "978-" + menosCaracacter
    numIsbn = []

    for num in masPrefijo:
        numIsbn = []
        if num == masPrefijo.isnumeric(num):
            numIsbn.append(num)
            parNum = 
            imparNum =
            for num in numIsbn:
                if numIsbn

                else:



    digitos12 = int()


    pass


if __name__ == '__main__':
    assert isbn_converter("1-85326-158-0") == "978-1-85326-158-9"
    assert isbn_converter("0-14-143951-3") == "978-0-14-143951-8"
    assert isbn_converter("0-02-346450-X") == "978-0-02-346450-8"
    assert isbn_converter("963-14-2164-3") == "978-963-14-2164-4"
    assert isbn_converter("1-7982-0894-6") == "978-1-7982-0894-6"