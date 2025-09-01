import sys
sys.path.append('')
from src.juego.contador_pintas import ContadorPintas

class CalzarInvalido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ArbitroRonda:
    def __init__(self):
        self.contador = ContadorPintas()

    # retorna true si la duda fue correcta (la apuesta se pasó) y false si la duda fue incorrecta
    def dudar(self, cachos, cantidad, pinta):
        return self.contador.contar(pinta, cachos) < cantidad
    
    # retorna true si la cantidad de pintas en la apuesta coincide exactamente con la cantidad de pintas en los dados y false si no lo hace
    def calzar(self, cachos, cantidad, pinta):
        cant_dados = 0
        for c in cachos:
            cant_dados += len(c.dados)
        mitad = (len(cachos)*5)/2
        if cant_dados < mitad:
            exc = CalzarInvalido(f"No se puede calzar, hay menos de {int(mitad)} dados")
            raise exc
        return self.contador.contar(pinta, cachos) == cantidad