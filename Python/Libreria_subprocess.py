# Invocación al sistema operativo: Ejecuta un comando de la terminal de forma aislada.
import subprocess

# - ["whoami"]: El comando se pasa como una lista para evitar vulnerabilidades de inyección.
# - capture_output=True: Redirige la salida de la terminal hacia la memoria de Python (evita que se imprima sola).
# - text=True: Traduce los bytes nativos del sistema a una cadena de texto (string) legible en Python.
result = subprocess.run(["whoami"],capture_output=True, text=True)


# Extracción de datos: Accede al atributo '.stdout' (Standard Output), que almacena el 
# texto plano que la terminal generó tras una ejecución exitosa.
print(result.stdout)