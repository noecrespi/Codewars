""" 
https://www.codewars.com/kata/58649884a1659ed6cb000072

Estás escribiendo código para controlar los semáforos de tu ciudad. Necesita una función para manejar cada cambio de green, a yellow, a redy luego a greenotra vez.

Complete la función que toma una cadena como argumento que representa el estado actual de la luz y devuelve una cadena que representa el estado al que debería cambiar la luz.

Por ejemplo, update_light('green')debería volver 'yellow'.
"""

VERDE = 'green'
AMARILLO = 'yellow'
ROJO = 'red'

def update_light(colorActual):
    # si el colorActual es 'verde'
    if colorActual == VERDE:
        # devuelve 'amarillo'
        return AMARILLO
    # si no el colorActual es 'amarillo'
    elif colorActual == AMARILLO:
        # devuelve 'rojo'
        return ROJO
    # sino 
    else:
        # devuelve 'verde'
        return VERDE
        