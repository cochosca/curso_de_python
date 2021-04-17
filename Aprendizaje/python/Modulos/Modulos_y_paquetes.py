#-------------------##
# MODULOS
#-------------------##
# Es un archivo con extensión .py. que puede definir funciones, clases y variables, también puede incluir código ejecutable.

# Este sirve Agrupando código relacionado para que el mismo sea mas fácil de entender y usar. Y MAS IMPORTANTE --MANTENIBLE--, es decir, que sea mas sencillo de modificar y que este sea escalable. Porque si ponemostodo el codigo del programa es sumamente dificil de corregir errores o optimizarlo

#------------------
# IMPORT
# -----------------
# Esta es utilizada para poder importar un modulo, QUE ESTA EN LA MISMA RUTA DE BUSQUEDA, o mas sencillo, en la misma carpeta
import Laboratorio_modulo

# ahora puedo utilizar todas sus variables, funciones, clases y metodos
helado = Laboratorio_modulo.comer('helado')

# Como el nombre del modulo es muy grande podemos asignarle otro nombre con la funcion 'as'
import Laboratorio_modulo as lm 
pancho = lm.comer('pancho')

# Para importar mas de un modulo se puende separar por comas
import Laboratorio_modulo, otro_metodo 
variable = Laboratorio_modulo.comer('pancho')
var2 = otro_metodo.cama('lumier')

#-----------##--------##
# PAQUETES
#-----------##--------##
# Son carpetas que contienen modulos y otros sub-paquetes.

# Para que pueda ser definido como paquete, el mismo tiene que tener un archivo __init__.py 

# --EJEMPLO--
# Si yo quiero que la carpeta paquete_ejemplo/ sea un paquete, le tengo que agregar el archivo vacio __init__.py a todas las carpetas de la ruta en donde esta
# 
# Aprendizaje/
#   __init__.py 
#   python/
#       __init__.py 
#       modulos/
#           __init__.py 
#           paquete_ejemplo/
#               __init__.py   

#-------------------
# FROM 
#-------------------
# Es una funcion que se complementa con import, lo que hace es permitir importar de un metodo
# Importar una funcion de un modulo
from Laboratorio_modulo import comer
pizza = comer('pizza')

# Si quiero importar todas las funciones, metodos, clases y variables del modulo
from Laboratorio_modulo import *
banquete = Comedor('banquete')
asado = comer('asado')

# Si quiero importar un modulo de un paquete que esta dentro de la misma ruta
from paquete_ejemplo import modulo_prueba as mp
gato = mp.gato('margarita')

# Si el paquete esta en otra ruta tenemos agregar despues del from toda la ruta de donde esta (--from Aprendizaje.python.Modulos.paquete_ejemplo.modulo_prueba import gato--) asi funciona en pychram pero en vs code se ponde la ruta desde la ubicion de este archivo
# aqui por ejemplo, como el modulo que queremos esta en la direccion Modulos/paquete_ejemplo/modulo_prueba.py y nosotros estamos en Modulos/Modulos_y_paquetes.py
from paquete_ejemplo.modulo_prueba import gato
s = gato('hola')
# si yo esta en el archivo laboratorio de pruebas tendria que ser asi
#from python.Modulos.otro_metodo import cama
# Ya que este esta detro de la carpete Aprendizaje/, la ruta de busqueda empiexa en la carpeta python/
