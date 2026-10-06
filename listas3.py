temperaturas = [28, 32, 31, 29, 34, 30, 33]
mayores = []

for temperatura in temperaturas:
    if temperatura > 30:
        mayores.append(temperatura)

print("Temperaturas mayores a 30:")
print(mayores)