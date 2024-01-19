#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:


largo =int(input("Lado: "))
longitud = largo + 2*(largo-1)
for i in range(largo):
    cadena =''
    for j in range(largo+2*i):
        cadena+='*'
    print(cadena.center(longitud))
for x in range(1,largo):
    cadena =""
    for j in range(2,largo+2*(largo-x),1):
        cadena+='*'
    print(cadena.center(longitud))
