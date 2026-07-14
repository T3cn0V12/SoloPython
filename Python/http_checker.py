import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2.0)

puerto = 80
direccion = "1.1.1.1"
mensaje_texto = "HEAD / HTTP/1.1\r\nHost: 1.1.1.1\r\n\r\n"
mensaje_bytes = mensaje_texto.encode()

try:
    s.connect((direccion,puerto))
    s.sendall(mensaje_bytes)
    respuesta = s.recv(1024)
    decodificada = respuesta.decode()
    print(decodificada)

except socket.timeout:
    print("El tiempo de espera excedio de 2s")

except ConnectionRefusedError:
    print("No se pudo hacer conexion con el puerto")

s.close()