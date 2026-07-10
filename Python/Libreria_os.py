import os

ejemplo = "algo"

#obtener direccion del ejecutable en el directorio de la pc
os.getcwd()

#Recibe una ruta como parametro y devuelve una lista de python con todos los nombres de los archivos 
# y subcarpetas que hay adentro
os.listdir()

#verifica si el archivo o la ruta dada existe o no, devolviendo un booleano
os.path.exists()

#Crear carpeta
os.mkdir("carpeta")

#Abrir un archivo y reescribir todo lo que hay, si no existe lo crea automaticamente
with open("registro.txt" ,"w") as archivo_salida:
    archivo_salida.write("Iniciando auditoria del sistema. \n")


#Abrir un archivo y agregarle algo a su contenido
with open("registro.txt" ,"a") as archivo_salida:
    archivo_salida.write("Nueva linea al historial de auditoria del sistema. \n")

#leer contenido de un archivo, equivalente al cat
with open("registro.txt" ,"r") as archivo_salida:
    contenido = archivo_salida.read()

print(contenido)