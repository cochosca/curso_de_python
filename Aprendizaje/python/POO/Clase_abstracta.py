# Primero tenemos que entender que es una intefaz de programacion, en la forma en la cual los objetos se comunican entre si
#----------------##
# CLASE ABSTRACTA
#----------------##
# Es una clase que define metodos y atributos que no estan implementados(que se definieron pero no se les agrego funcionalidad), a partir de esta clase no se pueden crear instancias, por lo que es obligatorio crear subclases, que a su vez crean sus propias implementaciones a los metodos abtactos de la clase abstracta, para evitar la dupliacion de codigo.

# Para poder crear una clase abstracta hay que importar el modulo abc y el decorador abstractmethod
from abc import ABC , abstractmethod

# la calse abstracta tiene que heredar de la clase ABC
class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
       self.ancho = ancho
       self.alto = alto
    # con el decorador @abstractmethod se determina que los metodos debajo son abstractos
    @abstractmethod
    def area(self):
        pass

# Ahora tenemos que crear si o si una subclase que cree la implementacion para poder crear un objeto porque con la clase abstracta no podemos crear un objeto directamente

class Cuadrado(FiguraGeometrica):
    def __init__(self,ancho,alto):
        super().__init__(ancho,alto)
    
    # realizamos la implementacion del metodo abstracto definido en FiguraGeometrica
    def area(self):
        return self.ancho * self.alto

cuadradito = Cuadrado(5,5)
print(cuadradito.area())