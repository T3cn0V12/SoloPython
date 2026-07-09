import os,subprocess
carpeta = "auditoria_servidor"

if os.path.exists(carpeta) == False:
    os.mkdir(carpeta)

with open(f"{carpeta}/archivo.txt", "w") as archivo:
    quiensoy = subprocess.run(["whoami"], capture_output=True, text=True)
    archivo.write(f"Sesion iniciada por el usuario {quiensoy.stdout}")

with open(f"{carpeta}/archivo.txt", "a") as archivo:
    archivo.write("Alerta! Acceso al sistema verificado \n")

print("Historial de auditoria actualizado de forma segura")