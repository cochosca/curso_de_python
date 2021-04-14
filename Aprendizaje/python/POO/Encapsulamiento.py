#-----------#----------------##
# ATRIBUTOS  Y METODOS PRIVADO DE PYTHON
#-----------#----------------##
# --Explicacion detallada: https://www.genbeta.com/desarrollo/cazadores-de-mitos-las-propiedades-privadas-en-python--
# Las variables «privadas» de instancia, que no pueden accederse excepto desde dentro de un objeto, no existen en Python
# Existen dos tipo,  publicos(que pueden ser consultados fuera de la clase) y privados (en donde no se puede modificar de forma externa de la clase)
# --ATRIBUTO PUBLICO--
class Comida:
    def __init__(self,platillo):
        self.platillo = platillo
    def retorna(self):
        return self.platillo
sopa = Comida('sopa paraguaya')
# este objeto se le puede obtener sus atributos
print(sopa.retorna())
# >>> sopa paraguaya
# --ATRIBUTO PRIVADO--
class Prueba:
    def __init__(self,p):
        self._p = p
    def vuelta(self):
        return self.p
prueba = Prueba('caca')
print(prueba.vuelta())
# >>> AttributeError: 'Prueba' object has no attribute 'p'
# Esto indica que no se puede acceder a ese atributo de forma externa, la unica forma es dento de la clase con la funcion get y set
class Prueba:
    def __init__(self,p):
        self._p = p
    def get_p(self):
        return self._p
prueba = Prueba('caca')
