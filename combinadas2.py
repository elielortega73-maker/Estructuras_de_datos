ventas = {
    "Lunes": [10, 20, 30],
    "Martes": [15, 25, 10],
    "Miércoles": [20, 20, 20]
}

for dia, datos in ventas.items():
    print(dia, ":", sum(datos))