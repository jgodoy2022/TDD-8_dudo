import sys
sys.path.append('')
from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self):
        pass

    def dudar(self, cachos, cantidad, pinta):
        con = ContadorPintas()
        return con.contar(pinta, cachos) < cantidad