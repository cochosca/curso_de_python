#--------##--------#
# CLASES
#--------##--------#
# Las clases son como plantillas, de donde se puede crear objetos, 
# los objetos son cosas individuales con caracteristica unicas
# Un toyota se diferencia de una Nissan por sus caracteristicas pero los dos son de la clase auto
class Auto: # EL NOMBRE DE LA CLASE SIEMPRE EMPIEZA EN MAYUSCULA
    def __init__(self,marca,tipo,modelo):
        self.mr = marca
        self.tp = tipo
        self.md = modelo
    def info(self):
        '''Retorna la informacion del auto ''' # Los docstrings sirven para docuemtar, osea si acercas el mouse al nombre de la funcion aparece lo que escribiste entre las tres comillas
        return self.mr, self.tp, self.md
# esta es la clase Auto, en donde tienen atributos preestablecidos
rav4_prime = Auto('toyota','suv','rav4')
juke = Auto('nissan', 'suv', 'juke')
print(f'los modelos de autos son {rav4_prime.info()} y {juke.info()}')
# >>> los modelos de autos son ('toyota', 'suv', 'rav4') y ('nissan', 'suv', 'juke')
# el objeto rav4_prime y juke son unicos cada uno pero los dos son de la misma clase
#-----------------
# CREAR UN OBJETO
#----------------
# Para crear un objeto se escribe en nombre del objeto y despues se pone la clase y se cargan los atributos
prius = Auto('toyota','sedan', 'prius')
#-----------------
# ATRIBUTOS
#-----------------
# Son las características que puede tener un objeto, como el color, forma, altura. etc
# Existen las VARIABLE DE CLASE, que son atributos que comparten todos los objetos de la clase
class Pelota:
    ''' las caracteristicas '''
    shape = 'round'
    color = 'red'
    size = '30 cm'
# Y  las VARIABLES DE INSTANCIA(crear un objeto a partir de una clase), que son atributos que tiene cada objeto de la clase
class Zapato:
    def __init__(self,marca,talle,tipo):
        self.mr = marca
        self.tl = talle
        self.tp = tipo
#-----------
# __INIT__ -- metodo especial
#----------
#El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.
# Es decir, en ese metodo se cargan los atributos(caracteristicas) de la clase, y en los siguientes metodos se realizan los algoritmos
class Auto:
    #El método __init__ es el primer método que se ejecuta cuando se crea un objeto, se llama automáticamente.
    def __init__(self,marca,tipo,modelo):
        self.mr = marca
        self.tp = tipo
        self.md = modelo
    # El método __init__ no puede retornar datos.
    # Para poder retonar datos creamos un metodo 
    def info(self):
        '''Retorna la informacion de los autos''' 
        return self.mr, self.tp, self.md 
rav4_prime = Auto('toyota','suv','rav4')
juke = Auto('nissan', 'suv', 'juke')
print(f'los modelos de autos son {rav4_prime.info()} y {juke.info()}')
# >>> los modelos de autos son ('toyota', 'suv', 'rav4') y ('nissan', 'suv', 'juke')
#------------
# SELF
#------------
