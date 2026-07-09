# Declaracion de contrasena maestra e input de la misma
password = "PTK0XY6W"
validacion = input("Ingresa tu password:")

# Validacion del acceso
if password == validacion:
    print("Acceso concedido. Bienvenido al sistema.")
else:
    print("Acceso denegado, contrasena incorrecta.")