dispositivo = {
    "modelo": "HP 250",
    "ip": "192.168.1.10",
    "estado": "Activo",
    "existencia": 5
}

print("Modelo:", dispositivo["modelo"])
print("IP:", dispositivo["ip"])
print("Estado:", dispositivo["estado"])

dispositivo["existencia"] = 10

print("Nueva existencia:", dispositivo["existencia"])