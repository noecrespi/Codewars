
# Paso de objetos mutables:
'''
def changer(X, lista_nueva):	# Arguments assigned references to objects
	X = 2			# Changes local name's value only
	lista_nueva[0] = 'spam' 	# Changes shared object in place	
	print(lista_nueva)
'''
'''
X = 1
lista_generada = [1, 2]
changer(1, lista_generada) # Caller: Pass immutable and mutable objects
print(X)
print(lista_generada)	# ['spam', 2]  # X is unchanged, L is different!
'''
'''
# Evitar que una routina modifique los elementos mutables:

# Opción 1:
X = 1
L = [1, 2]
changer(X, L[:]) 	# Pass a copy, so our 'L' does not change 
print(L)
'''
# Opción 2

def changer(a, b):
	copia_b = b[:]		# Copy input list so we don't impact caller
	a = 2
	copia_b[0] = 'spam'	# Changes our list copy only
	print(b)
	print(copia_b)


# Opción 3: convert to immutable objects:
X = 1
L = [1, 2] # pasar a tupla => tuple([1, 2]) => (1, 2)
changer(X, L)	# Pass a tuple, so changes are errors
print(L)
