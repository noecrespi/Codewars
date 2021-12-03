"""
Write a function that will check whether the permutation of an input string 
is a palindrome. Bonus points for a solution that is efficient and/or that 
uses only built-in language functions. Deem yourself brilliant if you can 
come up with a version that does not use any function whatsoever.

Example
madam -> True
adamm -> True ?????
junk -> False
"""

def isPalindrome(givenStr):
    '''
    Recorrer el literal en un sentido y comprobar si los caracteres opuestos
    coincidan. Cuando encontermos un carecter que no coincida con el opuesto,
    determinamos que el literal no es palíndromo.
    '''
    # intercambia espacios en blanco (' ') por caracter vacío ('')
    givenStrNoSpaces = givenStr.replace(' ', '')

    for (index, letter) in enumerate(givenStrNoSpaces):
        '''
            >>> 'pez payaso'.count('p')   
            # cuenta las veces que aparece el literal entre paréntesis  
            2
            >>> len('pez payaso')   
            # cuenta los caracteres
            10

            'larutanatural'[0] => 'l'
            'la ruta natural'[14] => 'l'

            'larutanatural'[0] == 'larutanatural'[11] ?? 

            len(givenStrNoSpaces) => número de caracteres empezando en 1
            len(givenStrNoSpaces) - 1) => último índice, número de posiciones empezando en 0

            -3 + 1 + 2= 0
            11 - 11 = 0
        '''

        if letter == givenStrNoSpaces[(len(givenStrNoSpaces) - 1) - index]: 
            continue
        else:
            print("{} is palindrome: False".format(givenStr))
            return False

    print("{} is palindrome: True".format(givenStr))
    return True




if __name__ == '__main__':

    assert isPalindrome('madam') == True
    assert isPalindrome('adamm') == False   # The exercise in the web expects True ??
    assert isPalindrome('junk') == False
    assert isPalindrome('ana') == True
    assert isPalindrome('la ruta natural') == True  # TODO: areglar caso test
    assert isPalindrome('no soy palíndromo') == False

