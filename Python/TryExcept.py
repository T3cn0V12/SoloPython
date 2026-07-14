elementos = [10, "cinco", 2, 0, "ocho", 5]

for i in elementos:
    try:
        resultado = 100/i
        print(f"100/{i} es igual a {resultado}")
    

    except TypeError:
        print("No se puede realizar la suma entre un numero y un texto")

    except ZeroDivisionError:
        print("No es posible dividir entre cero")