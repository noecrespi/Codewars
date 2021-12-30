""" 
Welcome young Jedi! In this Kata you must create a function that 
takes an amount of US currency in cents, and returns a 
dictionary/hash which shows the least amount of coins used 
to make up that amount. The only coin denominations considered 
in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) 
and Quarters (25¢). Therefor the dictionary returned should 
contain exactly 4 key/value pairs.

Notes:

If the function is passed either 0 or a negative number, the 
function should return the dictionary with all values equal to 0.
If a float is passed into the function, its value should be be 
rounded down, and the resulting dictionary should never contain 
fractions of a coin.

Examples

loose_change(56)    ==>  {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
loose_change(-435)  ==>  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
loose_change(4.935) ==>  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
"""



def loose_change(cents):

    '''
        1 Quarter => 25 Cents
        1 Dime => 10 Cents
        1 Nickel => 5 Cents
        1 Penny => 1 Cent
    '''

    coinsEquiv = {'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
    change = {'Pennies': 0, 'Nickels': 0, 'Dimes': 0, 'Quarters': 0}

    # devolver diccionario (change) sin nos dan 0 cents
    if cents <= 0:
        return change

    # cogerá en núm entero redondeandolo
    cents = int(cents) 

    # iterar para saber cuantas monedas hay de cada tipo
    for (key, value) in coinsEquiv.items():
        changeValue = int(cents / value)
        change[key] += changeValue 

        cents -= changeValue * value 

    return change



if __name__ == '__main__':
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(500) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 20}
