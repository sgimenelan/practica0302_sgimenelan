#Añadir una clase Pedido que tiene como atributos:
#    - lista de productos
#    - lista de cantidades
#Añade las siguiente funcionalidad:
#    - total_pedido: muestra el precio final del pedido
#    - mostrar_productos: muestra los productos del pedido
class Producto:

    __codigo = 0
    __nombre = ""
    __precio = 0

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, valor):
        self.__codigo = valor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, valor):
        self.__nombre = valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        self.__precio = valor

    def calculartotal(self, unidades):
        return self.__precio * unidades

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)

class Pedido:

    __productos = []
    __cantidades = []

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0
        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calculartotal(c)
        return total

    def mostrar_productos(self):
        for (p,c) in zip(self.__productos, self.__cantidades):
            print('Producto: ' + p.get_nombre() + ', Cantidad: ' + str(c))

p1 = Producto(1, "manzanas", 5)
p2 = Producto(2, "peras", 15)

productos = [p1,p2]
cantidades = [5, 10]

pedido = Pedido(productos, cantidades)
print('Total pedido: '+ str(pedido.total_pedido()) + "€")
pedido.mostrar_productos()