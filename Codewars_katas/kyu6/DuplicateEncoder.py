"""
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

El objetivo de este ejercicio es convertir una cadena en una nueva cadena donde cada carácter de la nueva cadena es "("si ese carácter aparece solo una vez en la cadena original, o ")"si ese carácter aparece más de una vez en la cadena original. Ignore las mayúsculas al determinar si un carácter es un duplicado.

Ejemplos
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

def duplicate_encode(texto):
    texto = texto.lower()
    variable = ''

    for letra in texto:
        numletra = texto.count(letra)
        if numletra > 1:
            variable += ')'
        else:
            variable += '('
    
    return variable
    