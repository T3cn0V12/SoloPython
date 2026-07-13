import socket

# 1. Crear el objeto socket
# AF_INET = IPv4, SOCK_STREAM = TCP ( saludo de 3 vías )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Configurar un timeout para que no se quede colgado esperando
s.settimeout(1.0)

# 3. Intentar la conexión (recibe una tupla: ('IP', puerto))
resultado = s.connect_ex(('127.0.0.1', 80))

# connect_ex devuelve 0 si la conexión fue exitosa (puerto abierto)
if resultado == 0:
    print("El puerto 80 está abierto")
else:
    print("El puerto 80 está cerrado o filtrado")

# 4. Cerrar el socket siempre al terminar
s.close()

#trae los bytes que el servidor haya enviado y guardalos en la memoria RAM
datos_crudos = s.recv(1024)
#1024 especifica el tamano del buffer en bytes, cuanta informacion desea recibir de un 
# solo golpe
#recv no devuelve str normal, devuelve bytes crudos

#para convertir esos datos en legibles se usa .decode()
texto = datos_crudos.decode()