import socket
puertos = [22,80,443]
direccion = "1.1.1.1"

for i in puertos:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    confirmacion = s.connect_ex((direccion,i))
    if confirmacion == 0:
        print(f"El puerto {i} esta abierto.")
    else:
        print(f"El puerto {i} esta cerrado")
    s.close()