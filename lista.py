dispositivos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora", "Tablet", "Celular", "Router"]

print("Dispositivos:")
print(dispositivos)

nuevo = input("Ingrese un nuevo dispositivo: ")
dispositivos.append(nuevo)

indice = int(input("Ingrese el índice que desea modificar: "))
nuevo_nombre = input("Ingrese el nuevo nombre: ")

dispositivos[indice] = nuevo_nombre

print("Lista final:")
print(dispositivos)