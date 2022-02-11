# 1. Argumentos y referencias compartidas


# Paso de objetos inmutables:

def  f ( b ):	 # una se le asigna a (referencias) el objeto pasado
    b  =  99  	# Cambia la variable local a solamente

b  =  88
f ( b )		 # a y b tanto referencia misma 88 inicialmente
print(b)