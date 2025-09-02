from src.juego.cacho import Cacho
from src.juego.validador_apuesta import ValidadorApuesta, Apuesta
from src.juego.contador_pintas import ContadorPintas
from src.juego.arbitro_ronda import ArbitroRonda, CalzarInvalido

class Jugador:
    def __init__(self, nombre, cantidad_dados=5):
        self.nombre = nombre
        self.cacho = Cacho(cantidad_dados)

    def perder_dado(self):
        self.cacho.perder_dado()

    def ganar_dado(self):
        self.cacho.ganar_dado()


class GestorPartida:
    def __init__(self, nombres_jugadores):
        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.turno_actual = 0
        self.validador = ValidadorApuesta()
        self.contador = ContadorPintas()
        self.arbitro = ArbitroRonda()  # 👈 agregado

    def jugador_actual(self):
        return self.jugadores[self.turno_actual]

    def siguiente_turno(self):
        vivos = [j for j in self.jugadores if j.cacho.cantidad_dados() > 0]
        if not vivos:
            return None
        idx = vivos.index(self.jugador_actual())
        self.turno_actual = (idx + 1) % len(vivos)
        return self.jugador_actual()

    def iniciar_ronda(self):
        for j in self.jugadores:
            if j.cacho.cantidad_dados() > 0:
                j.cacho.agitar()
        self.validador.apuesta_actual = None

    def procesar_apuesta(self, apuesta: Apuesta) -> bool:
        return self.validador.es_valida(apuesta)

    def procesar_dudo(self):
        apuesta = self.validador.apuesta_actual
        if apuesta is None:
            return None

        cachos = [j.cacho for j in self.jugadores]

        if self.arbitro.dudar(cachos, apuesta.cantidad, apuesta.pinta):
            idx_apostador = (self.turno_actual - 1) % len(self.jugadores)
            perdedor = self.jugadores[idx_apostador]
        else:
            perdedor = self.jugador_actual()

        perdedor.perder_dado()
        return perdedor

    def procesar_calzar(self, cacho_calzador):
        apuesta = self.validador.apuesta_actual
        if apuesta is None:
            return None

        cachos = [j.cacho for j in self.jugadores]
        try:
            if self.arbitro.calzar(cachos, apuesta.cantidad, apuesta.pinta, cacho_calzador):
                for j in self.jugadores:
                    if j.cacho != cacho_calzador and j.cacho.cantidad_dados() > 0:
                        j.perder_dado()
                return True
            else:
                calzador = [j for j in self.jugadores if j.cacho == cacho_calzador][0]
                calzador.perder_dado()
                return False
        except CalzarInvalido as e:
            raise e

    def juego_terminado(self):
        jugadores_vivos = [j for j in self.jugadores if j.cacho.cantidad_dados() > 0]
        return len(jugadores_vivos) == 1

    def ganador(self):
        if self.juego_terminado():
            return [j for j in self.jugadores if j.cacho.cantidad_dados() > 0][0]
        return None
