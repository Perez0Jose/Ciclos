#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:

#e=10!+11!+12!+13!+14!+…
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

#Recuerde que el factorial n! es el producto de los números de 1 a n.

import math
denominador=2
diferencia=1
euler = 2
fraccion1 = 1
fraccion2 = 1
while diferencia>0.0001:
    fraccion1 = fraccion2
    fraccion2= 1/math.factorial(denominador)
    denominador += 1
    euler += fraccion2
    diferencia= fraccion1-fraccion2
print(euler)








