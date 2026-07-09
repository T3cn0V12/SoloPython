historial = []
cont = 3

while cont > 0:
    evento = input("Que hizo el usuario?")
    cont -= 1
    historial.append(evento)

for i in historial:
    print(f"Incidente registrado: {i}")