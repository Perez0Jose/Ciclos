#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

altura = int(input("Altura:"))
ancho = int(input("Ancho: "))

for i in range(altura):
    for j in range(ancho):
        print("*", end="")
    print()