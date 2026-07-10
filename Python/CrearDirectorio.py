import os,subprocess
def Loadclear():
    subprocess.run(["sleep", "2"])
    os.system("clear")

nombre = input("Que nombre desea ponerle al directorio:")
os.mkdir(nombre)
print("Directorio creado...")
os.chdir(nombre)
Loadclear()

subcarpeta = input("Desea crear una subcarpeta? y/n:")
if subcarpeta == "y":
    total = input("Cuantas carpetas desea crear:")
    Loadclear()
    for i in range(1,int(total)+1):
        carpeta = input(f"Ingrese el nombre de la carpeta {i}:")
        os.mkdir(carpeta)
        print(f"La carpeta {carpeta} fue creada correctamente...")
        Loadclear()

Git = input("Desea crear un direcctorio git? y/n:")

if Git == "y":
    subprocess.run(["git", "init"])
    gitignore = input("Desea crear .gitignore? y/n:")
    if gitignore == "y":
        with open(".gitignore", "w") as f:
            pass
        print("gitignore creado correctamente...")
        Loadclear()

    readme = input("Desea crear un readme? y/n:")
    if readme == "y":
        with open("README.md", "w") as f:
            pass 
        print("README.md creado correctamente")
        Loadclear()

print("LISTO!")






