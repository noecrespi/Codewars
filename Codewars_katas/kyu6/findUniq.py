""" 
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

Hay una matriz con algunos números. Todos los números son iguales excepto uno. ¡Intenta encontrarlo!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

Se garantiza que la matriz contiene al menos 3 números.

Las pruebas contienen matrices muy grandes, así que piense en el rendimiento.
"""



def find_uniq(arr):
    
    contador = []
    for num in arr:
        
        if num == arr[1]:
            num ++1 
            contador.append(1)
        
        elif arr[0] != arr[1]:
            if arr[0] == arr[2]:
                return arr[1]
            else:
                return arr[0]
        
        else:
            return arr[len(contador)]




if __name__ == '__main__':
    assert find_uniq([ 3, 10, 3, 3, 3 ]) ==  10
    assert find_uniq([ 10, 3, 3, 3, 3 ]) ==  10
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
