import os
archivo_objetivo = "auth.log"

if os.path.exists(archivo_objetivo) == True:
    print(f"ÉXITO: Archivo de auditoría {archivo_objetivo} detectado. Procediendo con el análisis.")

else:
    print(f"ALERTA: No se encuentra el archivo {archivo_objetivo}. El sistema no está registrando eventos.")