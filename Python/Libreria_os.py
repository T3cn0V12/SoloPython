import os

#obtener direccion del ejecutable en el directorio de la pc
os.getcwd()

#Recibe una ruta como parametro y devuelve una lista de python con todos los nombres de los archivos 
# y subcarpetas que hay adentro
os.listdir("ruta")

#verifica si el archivo o la ruta dada existe o no, devolviendo un booleano
os.path.exists("ruta")