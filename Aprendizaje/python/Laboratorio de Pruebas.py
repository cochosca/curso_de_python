class Auto:
    def __init__(self,marca,tipo,modelo):
        self.mr = marca
        self.tp = tipo
        self.md = modelo
    def info(self):
        '''Retorna la informacion del auto '''
        return self.mr, self.tp, self.md
# esta es la clase Auto, en donde tienen atributos preestablecidos
rav4_prime = Auto('toyota','suv','rav4')
juke = Auto('nissan', 'suv', 'juke')
print(f'los modelos de autos son {rav4_prime.info()} y {juke.info()}')