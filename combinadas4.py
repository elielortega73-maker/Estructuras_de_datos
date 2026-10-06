estudiantes = {
    "Ana": [80, 90, 85],
    "Carlos": [70, 75, 80],
    "Pedro": [90, 95, 100]
}

for nombre, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    print(nombre, ":", promedio)