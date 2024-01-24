Algoritmo DivisoresPsint
	Definir i,indice,divisor,num Como Real;
	Escribir "Ingrese un numero: ";
	LEER num
	DIMENSION divisor(100)
	indice <- 1
	
	PARA i DESDE 1 HASTA RAIZ(num) HACER;
		SI num MOD i = 0 ENTONCES
			divisor(indice) <- i;
			indice <- indice + 1;
		FIN SI
	FIN PARA
	
	PARA i Desde indice-1 Hasta 1  Hacer;
		divisor(indice) <- num / divisor(i)
		indice <- indice + 1
	FIN PARA
	
	PARA i DESDE 1 HASTA indice - 1 HACER
		ESCRIBIR divisor(i), " ";
	FIN PARA
FinAlgoritmo
