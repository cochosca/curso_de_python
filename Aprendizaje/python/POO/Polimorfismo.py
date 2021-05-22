#----------------
# POLIMORFISMO
#---------------
# es cambiar la funcionalidad de un metodos en la clase hijo que fueron establecidos en la clase base, asi se adapta ese metodo a cada clase hija

# SOBRECARGA DE METODOS
class Padre:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f'hola pedrito, yo soy {self.nombre}')

class Hijo(Padre):
    def __init__(sefl, nombre):
        super().__init__(nombre)
    
    # sobrecarga del metodo, es decir, sobreescribir
    def hablar(self):
        print(f'hola juenito, yo soy {self.nombre}')


# SOBRECARGA DE OPERADORES
# Agregar nuevas funcionalidades a los operadores
class Sobrecarga():
    def __init__(self, nombre):
        self._nombre = nombre

    # metodo que sobreescribe 
    def __add__(self, other):   # Self va a hacer referencia primer operador y other al segundo
        return self._nombre + " y " + other._nombre

test1 = Sobrecarga('Roberto')
test2 = Sobrecarga('Juanito')
print(test1 + test2)
# >>> Roberto y Juanito

#METODOS PARA SOBRECARGAR DE LOS OPERADORES

# operadores binarios
# +  # __add__(sefl, other)
# -  # __sub__(sefl, other)
# *  # __mul__(sefl, other)
# /  # __truediv__(sefl, other) 
# // # __floordiv__(sefl, other) 
# %  # __mod__(sefl, other) 
# ** # __pow__(sefl, other) 

# operadores de comparacion
# <  # __it__(sefl, other) 
# >  # __gt__(sefl, other) 
# <= # __le__(sefl, other) 
# >= # __ge__(sefl, other) 
# == # __eq__(sefl, other)
# != # __ne__(sefl, other) 

# operadores de asignacion
# -=  # __isub__(sefl, other) 
# +=  # __iadd__(sefl, other) 
# *=  # __imul__(sefl, other)
# /=  # __idiv__(sefl, other) 
# //= # __iflorrdiv__(sefl, other) 
# %=  # __imod__(sefl, other) 
# **= # __ipow__(sefl, other) 

# operadores unitarios
# -  # __neg__(sefl, other) 
# +  # __pos__(sefl, other) 
# ~  # __invert__(sefl, other) 