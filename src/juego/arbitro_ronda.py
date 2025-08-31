import sys
sys.path.append('')
from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self):
        pass

    # retorna true si la duda fue correcta (la apuesta se pasó) y false si la duda fue incorrecta
    def dudar(self, cachos, cantidad, pinta):
        con = ContadorPintas()
        return con.contar(pinta, cachos) < cantidad
    
    def calzar(self, cachos, cantidad, pinta):
        con = ContadorPintas()
        return con.contar(pinta, cachos) == cantidad