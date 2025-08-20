import random

class Dado:
    def __init__(self):
        self.valor=None

    # Asigna valor random entre 1 y 6 (simula los valores de un dado de 6 caras)
    def tirar(self):
        self.valor=random.randint(1,6)
        return self.valor

    # Asigna una denominacion 
    def deno(self):
        denominaciones={1:"As",2:"Tonto",3:"Tren",4:"Cuadra",5:"Quina",6:"Sexto"}
        return denominaciones[self.valor]