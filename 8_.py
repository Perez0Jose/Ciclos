#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

#π=4(1−13+15−17+…)
#La entrada del programa debe ser un número entero n
 #que indique cuántos términos de la suma se utilizará.


n = int(input("Ingese un numero entero: "))
sum=0
for i in range(n):
    sum+=(-1)**(i)*(1/(2*i+1))
pi = 4 * sum
print(pi)