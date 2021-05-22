#-------------##
# EXCEPCIONES
#-------------##
# Las excepciones son bloques de código que nos permiten continuar con la ejecución de un programa pese a que ocurra un error.
# se utilza el comando try: para colocar el codigo que puede generar una excepcion
while True:
    try:
        n = int(input("-> coloca un numero: "))
        division = 10 / n
    # Este se ejecuta cuando occurre una excepcion, se usa la clase Exception porque es la mas genera, pero se puede poner clases de excepciones de menor jerarquia como ZeroDivisionError
    except Exception as e:
        print(f"Te equivocaste perro porque el denomidor no puede ser 0")
# # se puede agregar else cuando todo ocurrio de forma correcta
while True:
    try:
        n = int(input("-> coloca un numero: "))
        division = 10 / n
    except ZeroDivisionError():
        print("bobo")
    else:
        print("salio todo bien")
        break

# por ultimo se puede agregar el comando finally:, que este se ejecuta si o si cuando termina el codigo
while True:
    try:
        n = int(input("#--> coloca un numero: "))
        division = 10 / n
    except ZeroDivisionError:
        print("bobo")
    else:
        print("salio todo bien")
        break
    finally:
        print("-> Esta interaccion a terminado")

#----------------------
# EXCEPCIONES MULTIPLES
#----------------------
# Como en un bloque de codigo puede ocurrir errores distintos, a veces queremos actuar diferente con cada error
try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )

#-------------------------------------
# CREAR TUS PROPIAS CLASES EXCEPCIONES
#-------------------------------------
# siempre para poder crear tus excepciones tenes que heredar de la clase padre Exception
class ValoresIguales(Exception):
    def __init__(self, mensaje):
        self.message = mensaje


try:
    a = int(input("numero1 = "))
    b = int(input("numero2 = "))
    c = a + b 
    if a == b:
        raise ValoresIguales('Te equivocaste, no pueden ser iguales')
except Exception as e:
    print(e) # La clase exception es la que procesa ese error y cuando es impreso imprime el error que creamos