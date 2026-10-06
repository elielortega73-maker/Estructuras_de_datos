latencias = []

for i in range(10):
    latencia = float(input("Ingrese una latencia: "))
    latencias.append(latencia)

latencias.sort()

print("De menor a mayor:")
print(latencias)

latencias.sort(reverse=True)

print("De mayor a menor:")
print(latencias)