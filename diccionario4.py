ventas = {
    "Carlos": 500,
    "Ana": 800,
    "Pedro": 650
}

mayor = 0
tecnico = ""

for nombre, venta in ventas.items():
    if venta > mayor:
        mayor = venta
        tecnico = nombre

print("Mayor venta:", tecnico)
print("Cantidad:", mayor)