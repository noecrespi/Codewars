"""
https://www.codewars.com/kata/523a86aa4230ebb5420001e1

¿Qué es un anagrama? Bueno, dos palabras son anagramas entre sí si ambas contienen las mismas letras. Por ejemplo:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Escribe una función que encuentre todos los anagramas de una palabra de una lista. Se le darán dos entradas, una palabra y una matriz con palabras. Debe devolver una matriz de todos los anagramas o una matriz vacía si no hay ninguno. Por ejemplo:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


Problema: 
    buscar los anagramas 

Condiciones si son unos anagramas:
    si una palabra contiene las mismas letras y mismo numero de letras
    de letras que otra palabra == anagrama

Algoritmo:
    crear uns lista para meter los anagramas 
    iterar la lista de posibles anagramas 
        si la longitud de la palabra que nos dan es igual a la longitud del posible anagrama
        si la palabra contiene las mismas letras que el posible anagrama 
            guardar en la lista de angramas
    devolver la lista de nagramas 
"""



# definimos que la funcion <anagramas> recoge los argumentos de las <anagrama == 'str'> y <palabras == lista>
def anagrams(anagrama, palabras):
    # crear una variable tipo lisla 
    listaAnagrama = []
    #para cada palabra in words 
    for palabra in palabras:
        # si la longitud de la palabra es igaul a la longitud del anagrama
        # y si las letas de palabra son iguales a las letras de anagrama 
        if len(palabra) == len(anagrama) and set(palabra) == set(anagrama):
            listaAnagrama.append(palabra)
    return listaAnagrama
