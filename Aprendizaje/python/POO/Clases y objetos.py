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
# Existen las VARIABLE DE CLASE, que son atributos de la clase y que el obejto cuando es creado absorve esos atributos
# Estos se definen fuera de los metodos de clase
class Pelota:
    ''' las caracteristicas '''
    shape = 'round'
    color = 'red'
    size = '30 cm'
# Y  las VARIABLES DE INSTANCIA(crear un objeto a partir de una clase), que son atributos que tiene cada objeto de la clase y SOLO PUEDER SER ACCEDIDAS CUANDO CREAMOS EL OBJETO, a diferencia de las de clase que puede acceder a ellas ya que son atributos de la clase
# Estos se definen dentro de un metodo
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
# Es un paramtero que python carga de forma automatica, este sirve para que los metodos(funciones dentro de las clases) puedan usar los atributos que definimos en __init__
class Auto:
    def __init__(self,marca,tipo,modelo):    
        self.mr = marca # lo que hace es que comvierte el parametro marca en un atributo self.mr, entonces cuando crees metodos abajo solamente agregamos el parametro self y este hace como una referencia a todos los atributos que creamos
        self.tp = tipo
        self.md = modelo
    def info(self):# Solamente agregamos el parametro self y hace referencia a todos los atributos
        '''Retorna la informacion de los autos''' 
        return self.mr, self.tp, self.md # Retorna los atributos
#--------------
# AGREGAR UNA TUPLA A UN METODO
#--------------
# link: https://www.codigopiton.com/como-usar-asterisco-y-doble-asterisco-en-python/#:~:text=En%20Python%20el%20asterisco%20*%20se,y%20desempaquetar%20listas%20o%20tuplas.
# Para agregar una tupla se se pone al parametro un asterisco antes, al invocar a la función se empaquetan los diferentes valores proporcionados en dicha tupla y esta si o si tiene que estar al final para que python pudea asignar los valores de forma correcta, SOLAMENTE PUEDE EXISTIR UNA TUPLA EN UNA DEFINICION O METODO, tambien este parametro es opcional, es decir, no es necesarioa agregarle un valor para que se pueda crear el objeto
class Auto:
    def __init__(self,marca,tipo,modelo,*tupla): # NO SE PUEDE PONER OTRA PARAMETMRO DESPUES DE LA TUPLA           
        self.mr = marca
        self.tp = tipo
        self.md = modelo
        self.t = tupla
    def info(self):
        '''Retorna la informacion de los autos''' 
        return self.mr, self.tp, self.md, self.t # Retorna los atributo 
tesla = Auto('tesla', 'sedan', 'x',1,2,3,3,4,5,5,6,'hola')
print(tesla.info())
# >>> ('tesla', 'sedan', 'x', (1, 2, 3, 3, 4, 5, 5, 6, 'hola'))
#-----------------
# AGREGAR UN DICCIONARIO A UN METODO O DEF
#----------------
# Para agregar un diccionario se utilizan los dobles asteriscos, estos tienen que estar al final como las tuplas y pueden estas despues de ellas ya que su formato es diferentes a la de las tuplas y python los puede diferenciar facilmente
class Auto:
    def __init__(self,marca,tipo,modelo,*tupla,**diccionario): #          
        self.mr = marca
        self.tp = tipo
        self.md = modelo
        self.t = tupla
        self.d = diccionario
    def info(self):
        '''Retorna la informacion de los autos''' 
        return self.mr, self.tp, self.md, self.t, self.d# Retorna los atributo 
tesla = Auto('tesla', 'sedan', 'x',1,2,3,3,4,5,5,6,p=23,x=34,c=45,cd=23)# para el diccionario la clave es como una variable y el valor despues clave=valor, no clave:valor
print(tesla.info())
# >>> ('tesla', 'sedan', 'x', (1, 2, 3, 3, 4, 5, 5, 6), {'p': 23, 'x': 34, 'c': 45, 'cd': 23})
#---------------------
# METODOS ESTATICOS
#---------------------
# Son metodos de clase que no necesitan el paragemtro self ya que estos no estan relacionados con los objetos sino con la clase en si.
class MetodoEstatico:
    @staticmethod
    def metodo():
        print('mamahuebo')