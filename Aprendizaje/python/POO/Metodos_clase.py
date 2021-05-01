#-----------------
# METODOS DE CLASE
#-----------------
# Son metodos de la clase en si y no de los objetos que pueden ser creados con esa clase, estos metodos pueden llamar a variables de clase
class Clasesota:
    variable_clase = 25
    # metodo de clase, para determinarlo se utiliza el decorador @classmethod y para hacer referenica a las variable de clase de esta clase se agrega el argumento cls, es como utilizar self pero para metodo de clase
    @classmethod 
    def suma(cls):
        return cls.variable_clase + 34
    
    # metodo normal
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
# Estos metodo de clase sirven para realizar funciones sin crear un objeto y se llaman de esta forma
ropa = Clasesota.suma()
print(ropa)
# >>> 59
# si imprimimos para sabere que typo es la variable ropa podemos ver que no es un onjetos
print(type(ropa))
# >>> <class 'int'>

#-------------------
# METODO ESTATICO
#-------------------
# este es parecido a los metodos de clase pero a diferencia de este no es necesario agregar el parametro cls y este para referencia una variable de clase se tiene que poner clase.nombre_variable
class Sapo:
    sapito = 'robert'
    @staticmethod
    def nombre_sapo():
        print(Sapo.sapito)
sapote = sapo.nombre_sapo()
# >>> robert
# TANTO EL METODO DE CLASE Y EL ESTATICO NO PUEDEN OBTENER ATRIBUTOS YA QUE ESTOS TIENEN QUE ESTAR ESTABLECIDOS ANTES DE LLAMAR AL METODO
class Prueba:
    def __init__(self,nombre):
        self.nombre = nombre
    @classmethod
    def decime_tu_nombre(cls):
        print(cls.nombre)

pruebita = Prueba.decime_tu_nombre()
# >>> error perro