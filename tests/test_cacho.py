from unittest.mock import patch
from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_cacho_inicio():
    cacho = Cacho()
    assert len(cacho.dados) == 5
    assert hasattr(cacho,"dados_extra")

def test_agitar():
    v_validos = [1, 2, 3, 4, 5, 6]
    cacho=Cacho()
    cacho.agitar()

    for dado in cacho.dados:
        assert dado.valor in v_validos

def test_perder_dado():
    cacho = Cacho(5)
    cacho.perder_dado()
    assert len(cacho.dados) == 4

    cacho2 = Cacho(5)
    cacho2.dados_extra=2
    cacho2.perder_dado()
    assert len(cacho2.dados) == 5
    assert cacho2.dados_extra == 1

def test_ganar_dado():
    cacho = Cacho(2)
    cacho.ganar_dado()
    assert len(cacho.dados) ==3

    cacho2 = Cacho(5)
    cacho2.ganar_dado()
    assert len(cacho2.dados) == 5
    assert cacho2.dados_extra == 1

    cacho2.ganar_dado()
    assert cacho2.dados_extra == 2

def test_visibilidad():
    cacho = Cacho()

    # Estado inicial
    assert cacho.visible is True
    assert cacho.visible_demas is False

    # Cambiar visible
    cacho.ocultar()
    assert cacho.visible is False
    cacho.mostrar()
    assert cacho.visible is True

    # Cambiar visible_demas
    cacho.mostrar_demas()
    assert cacho.visible_demas is True
    cacho.ocultar_demas()
    assert cacho.visible_demas is False
