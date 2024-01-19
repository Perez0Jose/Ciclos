#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:

#12,14,18,116,132,164,…
#en forma decimal:

#0.5,0.25,0.125,0.0625,0.03125,0.015625,…
#El programa debe mostrar tres columnas que contengan la siguiente información:

#El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.

fraccion =1
i = 1
sum=0
union = ["Potencia", "Fracción", "Suma"]
for union in union:
    print(union, end="")
print()
while fraccion>0.000001:
    fraccion=1/(2**i)
    sum+=fraccion
    print(str(i).ljust(8), end="")
    print(str(round(fraccion,4)).ljust(8), end="")
    print(round(sum,4))
    i+=1










