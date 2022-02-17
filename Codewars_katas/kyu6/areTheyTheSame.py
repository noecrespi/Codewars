"""
https://www.codewars.com/kata/550498447451fbbd7600041c

Dadas dos matrices ay bescriba una función comp(a, b)(o compSame(a, b)) que verifique si las dos matrices tienen los "mismos" elementos, con las mismas multiplicidades (la multiplicidad de un miembro es el número de veces que aparece). "Igual" significa, aquí, que los elementos en bson los elementos en al acuadrado, independientemente del orden.

Ejemplos
Matrices válidas
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b)devuelve verdadero porque en b121 es el cuadrado de 11, 14641 es el cuadrado de 121, 20736 es el cuadrado de 144, 361 es el cuadrado de 19, 25921 es el cuadrado de 161, y así sucesivamente. Se vuelve obvio si escribimos blos elementos de en términos de cuadrados:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Matrices no válidas
Si, por ejemplo, cambiamos el primer número a otra cosa, compya no vuelve verdadero:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b)devuelve falso porque en b132 no es el cuadrado de ningún número de a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b)devuelve falso porque en b36100 no es el cuadrado de ningún número de a.

Observaciones
ao bpodría ser [] or {}(todos los idiomas excepto R, Shell).
ao bpuede ser nilo nullo Noneo nothing(excepto en C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift ).
Si ao bson nil(o nullo None, según el idioma), el problema no tiene sentido, por lo que devuelve falso.
"""



def comp(lista1, lista2):
    
    print(lista1)
    print(lista2)
    
    resultado = []
    
    #Si algunos de los dos no es nada, devuelveme False
    if lista1 == None or lista2 == None:
        return False
    
    #Si las dos listas estan vacias, devuelve True
    if not lista1 and not lista2:
        return True
    
    else:
        for elemento in range(0,len(lista1)):
        # de la lista 1 hay que elevar cada elemento a 2
        # pow(2, 2)
            operacion = pow(lista1[elemento], 2)
            resultado.append(operacion)

        resultado.sort()
        lista2.sort()

    if resultado == lista2:
        return True
    else:
        return False
