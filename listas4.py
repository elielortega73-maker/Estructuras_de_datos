existencias = [5, 0, 3, 0, 8, 0, 2]

agotados = 0

for i in range(len(existencias)):
    if existencias[i] == 0:
        print("Dispositivo agotado en la posición:", i)
        agotados += 1

print("Total agotados:", agotados)