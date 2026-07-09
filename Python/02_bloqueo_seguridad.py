# Declaracion de contrasena maestra e input de la misma
password = "PTK0XY6W"
cont = 3

while cont > 0:
    validacion = input("Ingresa tu password:")

    if validacion == password:
        print("Acceso concedido. Bienvenido al sistema")
        break
    
    cont -= 1

    if cont > 0:
        print("Acceso denegado.")
    else:
        print("Sistema bloqueado, se acabaron los intentos")