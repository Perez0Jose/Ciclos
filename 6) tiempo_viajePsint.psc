Algoritmo tiempo_viajePsint
	Definir t_viaje,total_t,total_min,total_seg,total_horas Como Real;
	Escribir "Duracion del tramo: ";
	Leer t_viaje;
	Mientras t_viaje <>0 Hacer;
		total_t<-total_t+t_viaje;
		Escribir "Duracion del tramo: ";
		Leer t_viaje;
	FinMientras
	total_min<- total_t;
    total_seg <- total_t MOD 1 * 60;
	total_horas<- total_t MOD 1 * 60;
	Escribir "Tiempo total de viaje ", total_horas , ":" ,total_min
FinAlgoritmo
