#Escriba un programa que entregue todos los divisores del número entero ingresado:

num = int(input("Ingrese un número:"))
divisors = []
for i in range(1,int(num**0.5)):
    if num%i==0:
        divisors.append(i)
for divisor in reversed(divisors):
    divisors.append(num/divisor)
print(divisors)









