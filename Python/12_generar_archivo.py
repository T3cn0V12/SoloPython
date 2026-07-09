import os
carpetalog = "logs_sistema"

if os.path.exists(carpetalog) == False:
    os.mkdir(carpetalog)

with open(f"{carpetalog}/archivo.txt" , "w") as archivo:
    archivo.write("Estado del sistema: Operacional \n")

print("Proceso de inicializacion completado")