class FrecuenciaTabla:
    ''' 
    Esta clase crea objetos como tablas de frecuencias, 
    necesitando solamente los datos brutos en forma de lista

    Atributos:
        datos_brutos = [lista de los numeros] 
    '''
    def __init__(self,datos_bruto):
        self.datos_bruto = datos_bruto
    
    def calcular_frecuencias(self):
        ''' Determina las varariables, calcula las frecuencias y 
        el porcentaje de las mismas.
        
        Frecuencias:
            - Frecuencia Absoluta[fi]: número de veces que aparece un 
            valor determinado en un estudio estadístico

            - Frecuencia Acumulada[fac]: Es la suma de la frecuencia 
            absoluta de x variable con con la frecuencia absoluta 
            anterior

            - Frecuancia Relativa[fr]: es el cociente entre la frecuencia 
            absoluta de un determinado valor y el número total 
            de datos

            - Frecuencia Relativa Acumulada[fr_ac]:Es la suma de la frecuencia 
            relativa de x variable con con la frecuencia absoluta 
            anterior

            - Porcentaje: porcentaje del total de la suma de todos los 
            datos que ocupa la frecuencia absoluta de x variable 

        Atributos:
            self.datos_brutos = datos_brutos
        '''
        def variable(self):
            '''Extrae los datos brutos y crea un set, para eliminar 
            los duplicados y obtener solamente las variables'''
            var = {dato for dato in self.datos_bruto} 
            var = list(var)
            self.var = var
            return self.var

        def fi(self):
            '''Calcula la frecuancia absoluta de cada variable'''
            frec_absoluta = [self.datos_bruto.count(i) for i in self.var]
            self.frec_absoluta = frec_absoluta
            return self.frec_absoluta
    
        def fac(self):
            '''Calcula la frecuencia acumulada de cada variable'''
            frec_acumulada = []
            acumulacion = int()
            for i in self.frec_absoluta:
                acumulacion +=i
                frec_acumulada.append(acumulacion) 
            self.frec_acumulada = frec_acumulada
            return self.frec_acumulada
    
        def fr(self):
            '''Calcula la frecuencia relativa de cada variable'''
            n = self.frec_acumulada[-1]    # n = cantidad todal de frecuencias
            frec_relativa = [round(i/n,2) for i in self.frec_absoluta]
            self.frec_relativa = frec_relativa
            return self.frec_relativa
    
        def fr_ac(self):
            '''Calcula la frecuencia relativa acumulada de 
            cada variable'''
            frec_rela_acumulada =[]
            acumulacion_rela = float()
            for n in self.frec_relativa:
                acumulacion_rela += n 
                frec_rela_acumulada.append(round(acumulacion_rela,1))
            self.frec_rela_acumulada = frec_rela_acumulada
            return self.frec_rela_acumulada
    
        def porcentaje(self):    
            '''Determina el porcentaje de cada variable'''
            porcentaje_var = ['{:1.1%}'.format(i*1) for i in self.frec_relativa]
            self.porcentaje_var = porcentaje_var
            return self.porcentaje_var
        return f''' --{variable(self)} \n --{fi(self)} \n --{fac(self)} \n --{fr(self)} 
        \n --{fr_ac(self)} \n --{porcentaje(self)}'''

    


prueba = FrecuenciaTabla( [4, 9, 85, 72, 95, 80, 24, 4, 85, 90])
print(prueba.calcular_frecuencias())
