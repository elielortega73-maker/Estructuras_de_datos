usuarios = {
    "Ana": "8888-1111",
    "Carlos": "8888-2222",
    "Pedro": "8888-3333"
}

nombre = input("Ingrese el nombre: ")

if nombre in usuarios:
    print("Teléfono:", usuarios[nombre])
else:
    print("Usuario no encontrado")