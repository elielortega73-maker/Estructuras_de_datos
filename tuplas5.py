def ventas(datos):
    total = sum(datos)
    promedio = total / len(datos)
    maxima = max(datos)

    return total, promedio, maxima


lista = [100, 200, 150, 300]

total, promedio, maxima = ventas(lista)

print("Total:", total)
print("Promedio:", promedio)
print("Venta máxima:", maxima)