evento1 = ["Ana", "Carlos", "Pedro", "Luis"]
evento2 = ["Carlos", "Pedro", "María"]

a = set(evento1)
b = set(evento2)

print("Asistieron a ambos:")
print(a & b)

print("Solo asistieron al primero:")
print(a - b)