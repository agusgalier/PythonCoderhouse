class Cliente:

    def __init__(self,nombre,edad,mail,direccion):

        self.nombre=nombre
        self.edad=edad
        self.mail=mail
        self.direccion=direccion
        self.carrito=[]


    def comprar(self):
        if len(self.carrito)>0:
            for item in self.carrito:
                print(f"Se ha comprado {item}") 
            print(f"Gracias por su compra {self.nombre},compra llegara dentro de 7 dias habiles en la direccion {self.direccion} se ha enviado un correo a {self.mail} con la factura")       
            self.carrito=[]
        else:
            print("El carrito esta vacio.No se pude realizar la compra")
    
    def añadir_carrito(self,item,tienda):
        self.carrito.append(item)
        print(f"Se ha guardado en el carrito el item {item} de la tienda {tienda}")

    def mostrar_carrito(self):
        if len(self.carrito)>0:
            print("Objetos en el carrito:")  
            for item in self.carrito:
                print(f"-{item}")
        else:
            print("El carrito esta vacio.")        


    def __str__(self):

        return (f"Se ha creado el cliente {self.nombre}")