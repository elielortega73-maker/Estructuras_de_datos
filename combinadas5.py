solicitudes = [
    {"cliente": "Ana", "dispositivos": ["Laptop", "Mouse"]},
    {"cliente": "Carlos", "dispositivos": ["Celular", "Tablet", "Router"]},
    {"cliente": "Pedro", "dispositivos": ["Monitor"]}
]

for solicitud in solicitudes:
    cantidad = len(solicitud["dispositivos"])
    print(solicitud["cliente"], "tiene", cantidad, "dispositivos")