#Escriba un programa que muestre una tabla de multiplicar como la siguiente y muestre los números alineados a la derecha.

for i in range(1,11):
    for j in range (1,11):
        product = str(i*j)
        if j==10:
            output=product.rjust(3)
        else:
            output=product.rjust(2)
        print(output, end=" ")
    print()








