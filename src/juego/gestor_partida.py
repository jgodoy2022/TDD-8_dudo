from src.juego.cacho import Cacho
from src.juego.validador_apuesta import ValidadorApuesta, Apuesta
from src.juego.contador_pintas import ContadorPintas
from src.juego.arbitro_ronda import ArbitroRonda, CalzarInvalido


class Jugador:
    def __init__(self, nombre, cantidad_dados=5):
        self.nombre = nombre
        self.cacho = Cacho(cantidad_dados)
        self.ronda_obligada = False  # indica si ya usó obligar

    def perder_dado(self):
        # El jugador pierde un dado de su cacho
        self.cacho.perder_dado()

    def ganar_dado(self):
        # El jugador gana un dado en su cacho
        self.cacho.ganar_dado()


class GestorPartida:
    def __init__(self, nombres_jugadores):
        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.turno_actual = 0
        self.validador = ValidadorApuesta()
        self.contador = ContadorPintas()
        self.arbitro = ArbitroRonda()
        self.ronda_especial = {
            "activo": False,
            "tipo": None,  # "abierta" o "cerrada"
            "jugador": None
        }

    def jugador_actual(self):
        return self.jugadores[self.turno_actual]

    def siguiente_turno(self):
        vivos = [j for j in self.jugadores if j.cacho.cantidad_dados() > 0]
        if not vivos:
            return None
        idx = vivos.index(self.jugador_actual())
        self.turno_actual = (idx + 1) % len(vivos)
        return self.jugador_actual()

    def iniciar_ronda(self, especial_tipo=None):
        """Inicia una ronda normal o especial si corresponde"""
        for j in self.jugadores:
            if j.cacho.cantidad_dados() > 0:
                j.cacho.agitar()
        self.validador.apuesta_actual = None

        jugador = self.jugador_actual()

        # Activar ronda especial si el jugador tiene 1 dado y no ha usado obligar
        if jugador.cacho.cantidad_dados() == 1 and not jugador.ronda_obligada:
            if especial_tipo is None:
                abierto = True
            else:
                abierto = especial_tipo == "abierta"

            if jugador.cacho.activar_ronda_especial(abierto=abierto):
                jugador.ronda_obligada = True
                self.ronda_especial["activo"] = True
                self.ronda_especial["tipo"] = "abierta" if abierto else "cerrada"
                self.ronda_especial["jugador"] = jugador

                # Ajustar visibilidad de todos los jugadores
                for j in self.jugadores:
                    if j == jugador:
                        continue
                    if abierto:
                        j.cacho.visible = False
                        j.cacho.visible_demas = True
                    else:  # cerrada
                        j.cacho.visible = False
                        j.cacho.visible_demas = False

                # Ajustar visibilidad del jugador especial
                if abierto:
                    jugador.cacho.visible = False
                    jugador.cacho.visible_demas = True
                else:
                    jugador.cacho.visible = True
                    jugador.cacho.visible_demas = False

    def finalizar_ronda_especial(self):
        if self.ronda_especial["activo"]:
            # Resetear todos los jugadores
            for j in self.jugadores:
                j.cacho.ronda_especial_activada = False
                j.cacho.visible = True
                j.cacho.visible_demas = False
            self.ronda_especial = {
                "activo": False,
                "tipo": None,
                "jugador": None
            }


    def procesar_apuesta(self, apuesta: Apuesta) -> bool:
        # Valida y registra la apuesta del jugador en turno
        return self.validador.es_valida(apuesta)

    def procesar_dudo(self):
        # Procesa la acción "Dudo"
        apuesta = self.validador.apuesta_actual
        if apuesta is None:
            return None

        cachos = [j.cacho for j in self.jugadores]

        if self.arbitro.dudar(cachos, apuesta.cantidad, apuesta.pinta):
            # El apostador pierde un dado
            idx_apostador = (self.turno_actual - 1) % len(self.jugadores)
            perdedor = self.jugadores[idx_apostador]
        else:
            # El que dudo pierde un dado
            perdedor = self.jugador_actual()

        perdedor.perder_dado()
        return perdedor

    def procesar_calzar(self, cacho_calzador):
        # Procesa la acción "Calzar" 
        apuesta = self.validador.apuesta_actual
        if apuesta is None:
            return None

        cachos = [j.cacho for j in self.jugadores]
        try:
            if self.arbitro.calzar(cachos, apuesta.cantidad, apuesta.pinta, cacho_calzador):
                # Todos menos el calzador pierden un dado
                for j in self.jugadores:
                    if j.cacho != cacho_calzador and j.cacho.cantidad_dados() > 0:
                        j.perder_dado()
                return True
            else:
                # El calzador falla y pierde un dado
                calzador = [j for j in self.jugadores if j.cacho == cacho_calzador][0]
                calzador.perder_dado()
                return False
        except CalzarInvalido as e:
            raise e

    def juego_terminado(self):
        # Retorna True si queda un jugador 
        jugadores_vivos = [j for j in self.jugadores if j.cacho.cantidad_dados() > 0]
        return len(jugadores_vivos) == 1

    def ganador(self):
        # Retorna el jugador ganador 
        if self.juego_terminado():
            return [j for j in self.jugadores if j.cacho.cantidad_dados() > 0][0]
        return None
    

