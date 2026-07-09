usuarios = {
    "root": "administrador",
    "tecno": "desarrollador", 
    "invitado": "solo lectura"
}

ingreso = input("Ingrese el nombre de usuario para consultar:")

if ingreso in usuarios:
    print(f"Usuario encontrado.Rol:{usuarios[ingreso]}")
else:
    print("Error: Usuario no registrado en el sistema")