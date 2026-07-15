import os,subprocess
IP_privada = subprocess.run(["ip", "a"],capture_output=True, text=True)
Gateway = subprocess.run(["ip", "route", "show"],capture_output=True, text= True)
MAC = subprocess.run(["ip", "neighbor"], capture_output=True, text=True)
ping = subprocess.run(["ping", "-c", "3", "1.1.1.1"],capture_output=True,text=True)

def busca(archivo,que,clave,donde,mensaje):
    with open(f"{archivo}", "w") as f:
        f.write(f"{que.stdout}")
    with open(f"{archivo}", "r") as f:
        Lectura = f.read()
        Busqueda = Lectura.splitlines()

    for i in Busqueda:
        if f"{clave}" in i:  
            lista = i.split()
            resultado = lista[donde]
            print(f"{mensaje}{resultado}")
            return resultado

    

ip_privada = busca("ip.txt",IP_privada,"global",1,"La IP privada en formato CIDR es:")
ip_gateway = busca("gateway.txt",Gateway,"default",2,"El gateway es:")
direccion_MAC = busca("MAC.txt",MAC,"dev",4,"La direccion MAC es:")
Ping = busca("Perdida.txt",ping,"received,",5,"El porcentaje de perdida de paquetes es:")

if Ping != "0%":
    trace = subprocess.run(["traceroute", "1.1.1.1"],capture_output=True,text=True)
    print(trace.stdout)