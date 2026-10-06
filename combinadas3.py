dispositivos = [
    {"nombre": "Laptop", "sistema": "Windows"},
    {"nombre": "Celular", "sistema": "Android"},
    {"nombre": "MacBook", "sistema": "macOS"},
    {"nombre": "Tablet", "sistema": "Android"}
]

sistemas = set()

for dispositivo in dispositivos:
    sistemas.add(dispositivo["sistema"])

print(sistemas)