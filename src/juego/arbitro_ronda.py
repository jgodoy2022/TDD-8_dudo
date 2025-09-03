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
    def dudar(self, cachos, cantidad, pinta, ronda_especial=False):
        return self.contador.contar(pinta, cachos, ronda_especial) < cantidad
    
    # retorna true si la cantidad de pintas en la apuesta coincide exactamente con la cantidad de pintas en los dados y false si no lo hace
    def calzar(self, cachos, cantidad, pinta, cacho_calzador, ronda_especial=False):
        jugador_valido = False
        if len(cacho_calzador.dados) == 1:
            jugador_valido = True
        cant_dados = 0
        for c in cachos:
            cant_dados += len(c.dados)
        mitad = (len(cachos)*5)/2
        if cant_dados < mitad and not jugador_valido:
            exc = CalzarInvalido(f"No se puede calzar, hay menos de {int(mitad)} dados y el jugador que calza tiene más de un dado")
            raise exc
        return self.contador.contar(pinta, cachos, ronda_especial) == cantidad