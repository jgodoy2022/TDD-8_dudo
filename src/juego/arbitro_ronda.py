import sys
sys.path.append('')
from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self):
        self.contador = ContadorPintas()

    # retorna true si la duda fue correcta (la apuesta se pasó) y false si la duda fue incorrecta
    def dudar(self, cachos, cantidad, pinta):
        return self.contador.contar(pinta, cachos) < cantidad
    
    # retorna true si la cantidad de pintas en la apuesta coincide exactamente con la cantidad de pintas en los dados y false si no lo hace
    def calzar(self, cachos, cantidad, pinta):
        con = ContadorPintas()
        return self.contador.contar(pinta, cachos) == cantidad