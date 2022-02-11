# 3. Valores predeterminados

# los valores predeterminados nos permiten hacer que los argumentos de función seleccionados sean opcionales; 
# si no se le pasa un valor, al argumento se le asigna su valor predeterminado antes de que se ejecute la función.

def  f ( a , b = 2 , c = 3 ): 	 # a requerida, b y c opcional
	print( a , b , c )


f ( 1 ) # 1  2  3
f ( a = 1 ) # 1  2  3


# Si pasamos dos valores, solo c obtiene su valor predeterminado, y con tres valores, no se utilizan valores predeterminados:

f ( 1 , 4 )     # 1  4  3
f ( 1 , 4 , 5 )	    # predeterminados # Override    # 1  4  5

f ( 1 , c = 6 )	 # Elija valores predeterminados    # 1  2  6