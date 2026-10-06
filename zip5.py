nombres = ["Ana", "Carlos", "Pedro"]
edades = [18, 20, 19]
ciudades = ["Managua", "Masaya", "Juigalpa"]

usuarios = []

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

    usuarios.append(usuario)

print(usuarios)