import pytest
from src.juego.gestor_partida import GestorPartida
from src.juego.validador_apuesta import Apuesta
from src.juego.dado import Dado

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

def test_ronda_especial_abierta():
    nombres = ["Alice", "Bob"]
    partida = GestorPartida(nombres)

    alice = partida.jugadores[0]
    bob = partida.jugadores[1]

    # Simular que Alice pierde dados hasta quedar con 1
    alice.cacho.dados = [Dado()]
    alice.cacho.dados[0].valor = 3
    assert alice.cacho.cantidad_dados() == 1

    partida.iniciar_ronda()

    # --- Verificar que la ronda especial abierta se activa ---
    assert partida.ronda_especial["activo"] is True
    assert partida.ronda_especial["tipo"] == "abierta"
    assert partida.ronda_especial["jugador"] == alice

    # Visibilidad de Alice y Bob durante la ronda
    assert alice.cacho.visible is False
    assert alice.cacho.visible_demas is True
    assert bob.cacho.visible is False
    assert bob.cacho.visible_demas is True

    # --- Probar acciones durante la ronda especial ---
    partida.apuesta_actual = Apuesta(1, "Tren")

    # Bob hace "dudar" usando el arbitro
    resultado_dudo = partida.arbitro.dudar(
        [j.cacho for j in partida.jugadores],
        partida.apuesta_actual.cantidad,
        partida.apuesta_actual.pinta,
        ronda_especial=True
    )
    assert isinstance(resultado_dudo, bool)

    # Bob hace "calzar" usando el arbitro
    resultado_calzar = partida.arbitro.calzar(
        [j.cacho for j in partida.jugadores],
        partida.apuesta_actual.cantidad,
        partida.apuesta_actual.pinta,
        bob.cacho,
        ronda_especial=True
    )
    assert isinstance(resultado_calzar, bool)

    # --- Finalizar la ronda ---
    partida.finalizar_ronda_especial()
    assert partida.ronda_especial["activo"] is False
    assert alice.cacho.visible is True
    assert alice.cacho.visible_demas is False
    assert alice.ronda_obligada is True
    assert bob.cacho.visible is True
    assert bob.cacho.visible_demas is False


def test_ronda_especial_cerrada():
    nombres = ["Alice", "Bob"]
    partida = GestorPartida(nombres)

    alice = partida.jugadores[0]
    bob = partida.jugadores[1]

    # Simular que Alice pierde dados hasta quedar con 1
    alice.cacho.dados = [Dado()]
    alice.cacho.dados[0].valor = 3
    assert alice.cacho.cantidad_dados() == 1

    # Iniciar ronda especial cerrada
    partida.iniciar_ronda(especial_tipo="cerrada")

    # --- Verificar que la ronda especial cerrada se activa ---
    assert partida.ronda_especial["activo"] is True
    assert partida.ronda_especial["tipo"] == "cerrada"
    assert partida.ronda_especial["jugador"] == alice

    # Visibilidad de Alice y Bob
    assert alice.cacho.visible is True
    assert alice.cacho.visible_demas is False
    assert bob.cacho.visible is False
    assert bob.cacho.visible_demas is False

    # --- Probar acciones durante la ronda especial ---
    partida.apuesta_actual = Apuesta(1, "Quina")

    # Bob hace "dudar" usando el arbitro
    resultado_dudo = partida.arbitro.dudar(
        [j.cacho for j in partida.jugadores],
        partida.apuesta_actual.cantidad,
        partida.apuesta_actual.pinta,
        ronda_especial=True
    )
    assert isinstance(resultado_dudo, bool)

    # Bob hace "calzar" usando el arbitro
    resultado_calzar = partida.arbitro.calzar(
        [j.cacho for j in partida.jugadores],
        partida.apuesta_actual.cantidad,
        partida.apuesta_actual.pinta,
        bob.cacho,
        ronda_especial=True
    )
    assert isinstance(resultado_calzar, bool)

    partida.finalizar_ronda_especial()
    assert partida.ronda_especial["activo"] is False
    assert alice.cacho.visible is True
    assert alice.cacho.visible_demas is False
    assert alice.ronda_obligada is True
    assert bob.cacho.visible is True
    assert bob.cacho.visible_demas is False
