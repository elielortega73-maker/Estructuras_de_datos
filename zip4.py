semana1 = [10, 20, 30, 15, 25, 18, 22]
semana2 = [12, 18, 35, 10, 30, 20, 25]

for dia1, dia2 in zip(semana1, semana2):
    diferencia = dia2 - dia1
    print("Diferencia:", diferencia)