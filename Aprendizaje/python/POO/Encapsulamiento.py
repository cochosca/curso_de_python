#-----------#----------------##
# ATRIBUTOS  Y METODOS PRIVADO DE PYTHON
#-----------#----------------##
# --Explicacion detallada: https://www.genbeta.com/desarrollo/cazadores-de-mitos-las-propiedades-privadas-en-python--
# En python realmente no existe metodos privados, lo que realmente exiten son formas de inidicar que ciertos atributos no deberias se accedidos fuera de la clase.
# TODAS LOS ATRIBUTOS SON PUBLICOS EN PYTHON
# --ATRIBUTO PUBLICO--
class Comida:
    def __init__(self,platillo):
        self.platillo = platillo
    def retorna(self):
        return self.platillo
sopa = Comida('sopa paraguaya')
# este objeto se le puede obtener sus atributos
print(sopa.platillo)
# >>> sopa paraguaya
# yo puedo modificar la variable de forma extena
sopa.platillo = 'sopa de chancho'
print(sopa.platillo)
# >>> sopa de chancho
# --ATRIBUTO PRIVADO-- 
# YO ESTOY INICANDO DE QUE NO SE DEVERIA ACCEDER DESDE AFUERA A OTRA PERSONA QUE ESTE LEYENDO ESTE CODIGO O A MI MISMO EN UN FUTURO
class Prueba:
    def __init__(self,p):
        self._p = p
# Con el guion bajo al comienzo se indica que este atributo es privado
popo = Prueba('caca')
print(popo._p)
# >>> caca
# yo puedo modificar igualmente pero NO DEBERIA porque lo indique anteriomente
popo._p = 'pipi'
print(popo._p)
# >>> pipi
#-------------------
# DOBLE GUION
#-------------------
# Son utilizados para renombrar ese atributo o metodo para que no coliciones con una subclase, es decir, di yo defini un atributo en una clase padre con doble guion este le cambia el nombre a : _Nombre_clase__nombre_atributo
class Padre:
    def __init__(self,caca,vaca = 34):
        self.__caca = caca
        self.vaca = vaca
ejemplo = Padre('hola','vaca')
print(dir(ejemplo))
# >>> ['_Padre__caca', ...] # El atributo se renombro

class Hijo(Padre):
    def __init__(self,caca, vaca):
        self.__caca = caca
        self.vaca
