"""
https://www.codewars.com/kata/541c8630095125aba6000c00

La raíz digital es la suma recursiva de todos los dígitos de un número.

Dado n, tome la suma de los dígitos de n. Si ese valor tiene más de un dígito, continúe reduciendo de esta manera hasta que se produzca un número de un solo dígito. La entrada será un número entero no negativo.

"""

def digital_root(n):
    n = str(n) 
    
    while len(n) != 1:
        str_to_int = []

        for char in n:
            str_to_int.append(int(char))

        add = 0

        for num in str_to_int:
            add = add + num
            
        n = str(add)

    return int(n)



if __name__ == '__main__':
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
    