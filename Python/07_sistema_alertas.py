def generar_alerta(componente, gravedad):
    if gravedad == "ALTA":
        return f"CRITICO, el componente {componente} reporta una falla grave"
    
    if gravedad == "BAJA":
        return f"INFO! el componente {componente} opera con normalidad"

print(generar_alerta("Cortafuegos", "ALTA"))
print(generar_alerta("Base de datos", "BAJA"))