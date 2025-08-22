from unittest.mock import patch
from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_cacho_inicio():
    cacho = Cacho()
    assert len(cacho.dados) == 5

def test_agitar():
    v_validos = [1, 2, 3, 4, 5, 6]
    cacho=Cacho()
    cacho.agitar()

    for dado in cacho.dados:
        assert dado.valor in v_validos

def test_perder_dado():
    cacho = Cacho()
    cacho.perder_dado()

    assert len(cacho.dados) < 5

def test_ganar_dado():
    cacho = Cacho(2)
    cacho.ganar_dado()

    cacho2 = Cacho(5)
    cacho2.ganar_dado()

    assert len(cacho.dados) ==3
    assert len(cacho2.dados) == 5

