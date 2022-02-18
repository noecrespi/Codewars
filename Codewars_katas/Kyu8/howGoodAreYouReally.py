"""
https://www.codewars.com/kata/5601409514fc93442500010b

Hubo un examen en tu clase y lo pasaste. ¡Felicidades!
Pero eres una persona ambiciosa. Quiere saber si es mejor que el estudiante promedio de su clase.

Recibe una matriz con los puntajes de las pruebas de sus compañeros. ¡Ahora calcule el promedio y compare su puntuación!

¡ Regresa Truesi estás mejor, de lo contrario False!

Nota:
Sus puntos no están incluidos en la matriz de puntos de su clase. ¡Para calcular el punto promedio, puede agregar su punto a la matriz dada!
"""



def better_than_average(notasClase , notaMia):
    totalNotas = 0 
    for nota in notasClase:
        totalNotas = nota + totalNotas 
        
    mediaClase = totalNotas / len(notasClase) 

    if mediaClase < notaMia:
        return True
    else:
        return False
