import pytest
import sys
sys.path.append('')
from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.cacho import Cacho
from src.juego.dado import Dado
from unittest.mock import patch

@patch('src.juego.dado.random.randint', return_value = 3)
def test_resultado_duda(mock_valor):
    cachos = []
    for i in range(2):
        c = Cacho(2)
        c.agitar()
        cachos.append(c)
    arbitro = ArbitroRonda()

    assert arbitro.dudar(cachos, 3, "Tren") is False
    assert arbitro.dudar(cachos, 2, "Tonto") is True


    cachos[0].dados[0].valor = 2
    assert arbitro.dudar(cachos, 4, "Tren") is True
    assert arbitro.dudar(cachos, 1, "Tonto") is False
    assert arbitro.dudar(cachos, 3, "Tonto") is True

    cachos[0].dados[1].valor = 1
    assert arbitro.dudar(cachos, 3, "Tren") is False
    assert arbitro.dudar(cachos, 4, "Tren") is True
    assert arbitro.dudar(cachos, 2, "Tonto") is False
    assert arbitro.dudar(cachos, 4, "Tonto") is True

@patch('src.juego.dado.random.randint', return_value = 3)
def test_resultado_calzar(mock_valor):
    cachos = []
    for i in range(2):
        c = Cacho(2)
        c.agitar()
        cachos.append(c)
    arbitro = ArbitroRonda()

    assert arbitro.calzar(cachos, 3, "Tren") is False
    assert arbitro.calzar(cachos, 4, "Tren") is True
    assert arbitro.calzar(cachos, 2, "Tonto") is False


    cachos[0].dados[0].valor = 2
    assert arbitro.calzar(cachos, 4, "Tren") is False
    assert arbitro.calzar(cachos, 3, "Tren") is True
    assert arbitro.calzar(cachos, 1, "Tonto") is True
    assert arbitro.calzar(cachos, 3, "Tonto") is False

    cachos[0].dados[1].valor = 1
    assert arbitro.calzar(cachos, 3, "Tren") is True
    assert arbitro.calzar(cachos, 2, "Tren") is False
    assert arbitro.calzar(cachos, 2, "Tonto") is True
    assert arbitro.calzar(cachos, 1, "Tonto") is False
    assert arbitro.calzar(cachos, 1, "As") is True