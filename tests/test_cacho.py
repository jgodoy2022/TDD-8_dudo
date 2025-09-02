from unittest.mock import patch
from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_cacho_inicio():
    # Al iniciar un cacho sin argumentos debe tener 5 dados
    cacho = Cacho()
    assert len(cacho.dados) == 5
    # Debe tener el atributo dados_extra para manejar dados adicionales
    assert hasattr(cacho, "dados_extra")


def test_agitar():
    # Al agitar, cada dado debe obtener un valor válido entre 1 y 6
    v_validos = [1, 2, 3, 4, 5, 6]
    cacho = Cacho()
    cacho.agitar()

    for dado in cacho.dados:
        assert dado.valor in v_validos


def test_perder_dado():
    # Caso 1: perder un dado normal (sin dados_extra)
    cacho = Cacho(5)
    cacho.perder_dado()
    assert len(cacho.dados) == 4

    # Caso 2: si tiene dados_extra, no se pierde del set principal
    cacho2 = Cacho(5)
    cacho2.dados_extra = 2
    cacho2.perder_dado()
    assert len(cacho2.dados) == 5  # se mantienen los mismos dados
    assert cacho2.dados_extra == 1  # pero se reduce en los extras


def test_ganar_dado():
    # Caso 1: con menos de 5 dados, se gana uno en la lista principal
    cacho = Cacho(2)
    cacho.ganar_dado()
    assert len(cacho.dados) == 3

    # Caso 2: con 5 dados, no aumenta la lista principal, solo dados_extra
    cacho2 = Cacho(5)
    cacho2.ganar_dado()
    assert len(cacho2.dados) == 5
    assert cacho2.dados_extra == 1

    # Ganar nuevamente aumenta dados_extra
    cacho2.ganar_dado()
    assert cacho2.dados_extra == 2


def test_visibilidad():
    cacho = Cacho()

    # Estado inicial
    assert cacho.visible is True
    assert cacho.visible_demas is False

    # Cambiar atributo visible (propio jugador)
    cacho.cambiar_mostrar()
    assert cacho.visible is False
    cacho.cambiar_mostrar()
    assert cacho.visible is True

    # Cambiar atributo visible_demas (otros jugadores)
    cacho.cambiar_mostrar_demas()
    assert cacho.visible_demas is True
    cacho.cambiar_mostrar_demas()
    assert cacho.visible_demas is False
