#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

time_traveling = int(input("Duración del tramo: "))
total_time=0
while time_traveling!=0:
    total_time+=time_traveling
    time_traveling = int(input("Duracion del tramo: "))
print(f"Tiempo total de viaje: {total_time//60}:{str(total_time%60).zfill(2)} horas")
















