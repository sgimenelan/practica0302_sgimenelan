#Crear una Clase Producto con los siguientes atributos:
# - código
# - nombre
# - precio 
# Crea su constructor, getter y setter y una función llamada
# calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.
class Producto():

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    def __str__(self):
        return "Codigo: " + str(self.__codigo) + ", Nombre: " + str(self.__nombre) + ", Precio: " + str(self.__precio)
    
    def calculartotal(self, ud):
        total = self.__precio * ud
        return "El precio total de " + str(self.__nombre) + " es " + str(total)
    
p1 = Producto(1, "Television", 350)
p2 = Producto(2, "Telefono", 1000)


print(p1.calculartotal(10))
print(p2.calculartotal(10))




