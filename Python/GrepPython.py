import os
directorio = "diagnostico_red"

if os.path.exists(directorio) == False:
    os.mkdir(directorio)

with open(f"{directorio}/trazado.txt", "w") as trazado:
    trazado.write("1  10.0.2.2 (10.0.2.2)  5.999 ms\n 2  10.0.2.2 (10.0.2.2)  3.941 ms\n --- FIN DEL DIAGNOSTICO ---\n")

with open(f"{directorio}/trazado.txt", "r") as trazado:
    contenido = trazado.readlines()

for i in contenido:
    if "10.0.2.2" in i:
        print(f"Registro encontrado -> {i}")
