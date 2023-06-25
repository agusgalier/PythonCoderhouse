from mi_paquete.modulo1 import Cliente

cliente=Cliente(input("Ingrese su nombre:"),input("ingrese su edad:"),input("ingrese su mail:"),input("ingrese su direccion:"))
print (cliente)

menu=True
while menu:
    print("""
    =================
          MENÚ
    =================
    1. Añadir productos al carro
    2. Mostar carrito
    3. Realizar compra
    4. Salir
    """)

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        bandera=True
        while bandera:
            producto=input("ingrese el producto que desea comprar en caso de no querer agregar mas productos ingrese (salir):")
           
            if producto.lower()=="salir":
                break
            else:
                supermercado=input("""
                Supermercados disponibles:
                -Walmart
                -Jumbo
                -Coto
                ingrese un supermercado:
                """)
            cliente.añadir_carrito(producto,supermercado)
    elif opcion == 2:
        cliente.mostrar_carrito()
    elif opcion == 3:
        cliente.comprar()
    elif opcion == 4:
        print("Hasta luego")
        menu = False
    else:
        print("Ingrese una opción válida")