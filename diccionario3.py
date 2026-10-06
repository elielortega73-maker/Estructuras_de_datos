accesos = ["Laptop", "Celular", "Laptop", "Tablet", "Celular", "Laptop"]

conteo = {}

for dispositivo in accesos:
    if dispositivo not in conteo:
        conteo[dispositivo] = 0

    conteo[dispositivo] += 1

print(conteo)