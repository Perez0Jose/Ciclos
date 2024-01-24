Algoritmo Suma_entre_numerosPsint
	Definir num1,num2,sum,i Como Real;
	Escribir "Ingrese un numero: ";
	Leer num1
	Escribir "Ingrese otro numero: ";
	Leer num2
	
	Para i<-num1+1 Hasta num2-1 Hacer;
		sum<- sum+i;
	FinPara
	Escribir "La suma es ",sum;
FinAlgoritmo
