blacklist = ["192.168.1.50", "10.0.0.99", "18.200.5.12"]

ingreso = input("Ingrese una direccion IP:")

if ingreso in blacklist:
    print("ALERTA: Tráfico bloqueado. IP maliciosa detectada.")
else:
    print("Acceso permitido: IP limpia.")