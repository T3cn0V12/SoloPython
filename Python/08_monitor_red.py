servidores = {
    "192.168.1.10": "ACTIVO", 
    "192.168.1.20": "CAÍDO", 
    "192.168.1.30": "ACTIVO",
    "192.168.1.40": "CAÍDO"
}

def evaluar_sistema(estado):
    if estado == "CAÍDO":
        return "Alerta, servidor fuera de linea. Revisar inmediatamente!"
    
    if estado == "ACTIVO":
        return "Operando normalmente..."

for j, i in servidores.items():
    print(f"Servicio {j}:{evaluar_sistema(i)}")