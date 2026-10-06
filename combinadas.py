dispositivos = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Mouse", "precio": 20},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Teclado", "precio": 30}
]

valor = 100

for dispositivo in dispositivos:
    if dispositivo["precio"] > valor:
        print(dispositivo["nombre"])