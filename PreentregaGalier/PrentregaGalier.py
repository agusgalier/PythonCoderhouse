import json

def Registro():
    with open("PreentregaGalier/usuarios.json", "r") as archivo:
        usuarios = json.load(archivo)

    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasenia = input("Ingrese la contraseña: ")

    nuevo_usuario = {
        "nombre": nombre_usuario,
        "contraseña": contrasenia
    }
    usuarios.append(nuevo_usuario)

    with open("PreentregaGalier/usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

    print("Se ha registrado el usuario correctamente")

def mostrar_usuario():
    with open("PreentregaGalier/usuarios.json", "r") as archivo:
        usuarios = json.load(archivo)
    print("Usuarios registrados:")
    for usuario in usuarios:
        print("Usuario:", usuario["nombre"])
        print("----------")

def login():
    with open("PreentregaGalier/usuarios.json", "r") as archivo:
      usuarios = json.load(archivo)
    iniciar_usuario = input("Ingrese el usuario: ")
    iniciar_contrasenia = input("Ingrese la contraseña: ")

    for usuario in usuarios:
        if usuario["nombre"] == iniciar_usuario and usuario["contraseña"] == iniciar_contrasenia:
            print("Se ha iniciado sesión correctamente")
            return

    print("Los datos ingresados son incorrectos")

menu = True
while menu:
    print("""
    =================
          MENÚ
    =================
    1. Iniciar sesión
    2. Registrar usuario
    3. Mostrar usuarios
    4. Salir
    """)

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        login()
    elif opcion == 2:
        Registro()
    elif opcion == 3:
        mostrar_usuario()
    elif opcion == 4:
        print("Hasta luego")
        menu = False
    else:
        print("Ingrese una opción válida")