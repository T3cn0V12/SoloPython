import os, subprocess
nombre_carpeta = "seguridad_auditoria"
if os.path.exists(nombre_carpeta) == False:
    os.mkdir(nombre_carpeta)
    quiensoy = subprocess.run(["whoami"], capture_output=True, text=True)
    print(f"Directorio {nombre_carpeta} creado exitosamente por el usuario:{quiensoy.stdout}")
else:
    print(f"Acceso denegado: el directorio {nombre_carpeta} ya existe.")
