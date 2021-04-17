''' Esta es la documentacin del modulo'''
def comer(platillo):
    print('mmmmm que rico')

class Comedor:
    def __init__(self,platillo):
        self.__platillo = platillo
    def __str__(self):
        return f'Comedor de {self.__platillo}'