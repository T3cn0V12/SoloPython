puertos = [21, 22, 88, 443, 3306, 8080]

for i in puertos:
    if i == 21 or i == 3306:
        print(f"Puerto {i}: Riesgo critico (FTP/MySQl) expuesto.")
    else:
        print(f"Puerto {i}: puerto seguro/monitoreado")