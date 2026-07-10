import os,subprocess
#Archivo a revisar
file = input("Ingrese el nombre de su archivo a verificar:")
permiso = True
#Comprobar que la extension sea .sh

#En caso de que no exista o sea incompatible
if not file.endswith(".sh"):
    print("El archivo ingresado es incompatible con .sh, el programa ha terminado.")

elif not os.path.exists(file):
    print("El archivo ingresado es inexistente, el programa ha terminado.")

#En caso de que exista 
else:
    #Se abrira el archivo y se guardaran sus lineas en una lista
    with open(f"{file}", "r")as f:
        recuperado = f.readlines()

    #Verificar si algun comando se esta corriendo con el superusuario sudo
    for i in recuperado:
        #Si es asi si bloquera el archivo y terminara el programa
        if "sudo" in i:
            print(f"El archivo {file} ha sido bloqueado por politicas de seguridad, la operacion ha terminado")
            permiso = False
            break

#Verificado lo anterior se cambiaran los permisos con chmod 755
if permiso == True:
    print("El archivo ha sido aprobado, en este momento se estan acualizando los permisos...")
    subprocess.run(["sleep", "5"])
    os.system("clear")
    print("Los permisos fueron actualizados sastifactoriamente. Programa terminado")
    os.chmod(f"{file}", 0o755)