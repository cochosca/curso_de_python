#------------------##
# HERENCIA
#------------------##
# Cuando hay una clase principal o padre que herede sus metosod y atributos a las subclases o clases hijo
class Principal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
# la clase Principal tiene los atributos nombre y edad
class Secundaria(Principal):# Entre parentesis se pone la clase de donde se hereda, en este caso de la clase Principal
    def __init__(self,nombre,edad,pie,mano):
        super().__init__(nombre,edad) # el comando super().metodo() lo que hace en referenciar a los atributos que fueron heredados de la clase anterior
        self.pie = pie 
        self.mano = mano
    def __str__(self):
        return self.pie

pepe = Secundaria('pepe', 15, 'chico', 'grande')
print(pepe)
#--------------------
# __STR___
#____________________
# Su funcion es que el objeto sea mas legible, ya que el mismo retona una cadena de texto
class Pedro:
    def __init__(self,c):
        self.c = c
pedro = Pedro('c')
print(pedro)
# >>> <__main__.Pedro object at 0x7f0e75bd3790>
# Con el metodo __str__ podemos hacer al imprimir el objeto en si sea mas legible
class Pedrito(Pedro):
    def __init__(self,c,sapo,gato):
        super().__init__(c)
        self.sapo = sapo
        self.gato = gato
    def __str__(self):
        return f'la variable es: {self.sapo}'
pato = Pedrito('c', 'hola', 'chau')
print(pato)
# >>> la variable es: hola
#------------------
# HERENCIA MULTIPLE
#------------------
# Consiste en que una subclase puede heredear de muchas clases principales
class Padre:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f'Clase padre, su nombre es {self.nombre} y su apellido es {self.apellido}'
print(Padre('jose','bentiez'))
class Madre:
    def __init__(self,altura,peso):
        self.altura = altura
        self.peso = peso

# Clase que hereda de padre y madre
class Hijo(Padre,Madre):
    def __init__(self,nombre,apellido,altura,peso,oficio):
       # se llama el nombre de la clase y su atributo __init__(parametros a traer)
        Padre.__init__(self,nombre,apellido) 
        Madre.__init__(self,altura,peso)
        self.oficio = oficio