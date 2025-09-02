import pytest
from src.juego.gestor_partida import GestorPartida
from src.juego.validador_apuesta import Apuesta


@pytest.fixture
def partida():
    # Crea una partida con dos jugadores: YO y TU
    return GestorPartida(["YO", "TU"])


def test_iniciar_partida(partida):
    # Ambos jugadores empiezan con 5 dados
    assert all(j.cacho.cantidad_dados() == 5 for j in partida.jugadores)


def test_apuesta_valida(partida):
    # Una apuesta inicial válida debe ser aceptada
    partida.iniciar_ronda()
    resultado = partida.procesar_apuesta(Apuesta(1, 2))  # 1 tonto
    assert resultado is True
    assert partida.validador.apuesta_actual.cantidad == 1
    assert partida.validador.apuesta_actual.pinta == 2


def test_dudo_hace_perder_dado(partida):
    # Al dudar, alguien pierde un dado (apostador o dudador)
    partida.iniciar_ronda()
    partida.procesar_apuesta(Apuesta(1, 2))  # Jugador 1 apuesta
    partida.siguiente_turno()

    perdedor = partida.procesar_dudo()
    assert perdedor is not None
    # El perdedor debería quedar con 4 dados
    assert perdedor.cacho.cantidad_dados() == 4


def test_juego_termina(partida):
    # El juego termina cuando un jugador se queda sin dados
    jugador1 = partida.jugadores[0]
    jugador2 = partida.jugadores[1]

    for _ in range(5):
        jugador1.perder_dado()

    assert jugador1.cacho.cantidad_dados() == 0
    assert jugador2.cacho.cantidad_dados() == 5
    assert partida.juego_terminado() is True
    assert partida.ganador() == jugador2
