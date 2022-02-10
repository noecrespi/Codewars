""" 
https://www.codewars.com/kata/517abf86da9663f1d2000003

Complete el método/función para que convierta las palabras delimitadas por guiones/guiones bajos en mayúsculas y minúsculas. La primera palabra dentro de la salida debe estar en mayúsculas solo si la palabra original estaba en mayúsculas (conocido como Upper Camel Case, también conocido como caso Pascal).

Ejemplos
"the-stealth-warrior"se convierte en "theStealthWarrior"
"The_Stealth_Warrior"se convierte en"TheStealthWarrior"
"""

"""
algoritmo:
1. convertir todos los guiones / subrayados a solo uno de los mismos ["the-stealth_warrior"]
    - https://docs.python.org/es/3/library/stdtypes.html#str.replace
2. substraer las palabras en una lista
    - https://docs.python.org/es/3/library/stdtypes.html?highlight=split#str.split
3. convertir la primera letra de cada palabra en mayuscula
    - https://docs.python.org/es/3/library/stdtypes.html?highlight=str%20capitalize#str.capitalize
4. concatenar las palabras
    - https://docs.python.org/es/3/library/stdtypes.html?highlight=join#str.join
# .append = metodo https://docs.python.org/es/3/library/array.html?highlight=append#array.array.append
casos test:
- la primera palabra NO debe modificarse

"""

def to_camel_case(text):            # text = 'the-stealth_warrior'
    # modifica text y reemplaza '-' por '_'
    text = text.replace('-' , '_')  # text = 'the_stealth_warrior'
    # guarda la lista de palabras separadas por '_'
    listpalabras = text.split('_')  # listpalabras = ['the' , 'stealth' , 'warrior']
    # crea una lista vacia
    primermayuscula = []
    # crea la posicion y dale valor 0
    posicion = 0 

    # para cada palabra dentro de listpalabras
    for palabra in listpalabras:
        # si posicion es igual a 0
        if posicion == 0:
            # mete en la lista la palabra
            primermayuscula.append(palabra)
        # si no es la posicion 0
        else:
            # mete en la lista la palabra CON la primera mayuscula
            primermayuscula.append(palabra.capitalize())    # primermayuscula = [palabra, palabra, palabra, ...]
        # suma una posicion
        posicion = posicion + 1

    # devolver las palabras concatenadas
    return ''.join(primermayuscula)