import os
ubicacion = os.getcwd()
elementos = os.listdir(".")

print(f"Explorando la ruta: {ubicacion}")
for i in elementos:
    print(f"Elemento detectados {i}")
