import os ,subprocess
dir_red = "reportes_red"
if os.path.exists(dir_red) == False:
    os.mkdir(dir_red)

with open(f"{dir_red}/ping_log.txt","w") as archivo:
    Pings = subprocess.run(["ping", "-c", "3", "127.0.0.1"],capture_output=True, text=True)
    archivo.write(Pings.stdout)

with open(f"{dir_red}/ping_log.txt","a") as archivo2:
    archivo2.write("--- DIAGNOSTICO FINALIZADO CON EXITO --- \n")

with open(f"{dir_red}/ping_log.txt","r") as archivo3:
    print(archivo3.read())