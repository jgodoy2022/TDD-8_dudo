import pytest
import sys
sys.path.append('')
from src.juego.arbitro_ronda import ArbitroRonda, CalzarInvalido
from src.juego.cacho import Cacho
from unittest.mock import patch

# Si el resultado de dudar() es True, la duda fue válida y pierde quien apostó,
# si el resultado de dudar() es False, la duda fue equívoca y pierde quien dudó
@patch('src.juego.dado.random.randint', return_value=3)
def test_resultado_duda(mock_valor):
    # Configura dos cachos con dados fijos para test de dudar
    cachos = []
    for i in range(2):
        c = Cacho(2)
        c.agitar()
        cachos.append(c)
    arbitro = ArbitroRonda()

    # Pruebas básicas de dudar
    assert arbitro.dudar(cachos, 3, "Tren") is False
    assert arbitro.dudar(cachos, 2, "Tonto") is True

    # Modificando algunos dados manualmente
    cachos[0].dados[0].valor = 2
    assert arbitro.dudar(cachos, 4, "Tren") is True
    assert arbitro.dudar(cachos, 1, "Tonto") is False
    assert arbitro.dudar(cachos, 3, "Tonto") is True

    # Combinando comodines
    cachos[0].dados[1].valor = 1
    assert arbitro.dudar(cachos, 3, "Tren") is False
    assert arbitro.dudar(cachos, 4, "Tren") is True
    assert arbitro.dudar(cachos, 2, "Tonto") is False
    assert arbitro.dudar(cachos, 4, "Tonto") is True

    # Ronda Especial (As no es comodín)
    ronda_especial = True
    assert arbitro.dudar(cachos, 3, "Tren", ronda_especial) is True
    assert arbitro.dudar(cachos, 2, "Tren", ronda_especial) is False
    assert arbitro.dudar(cachos, 2, "Tonto", ronda_especial) is True
    assert arbitro.dudar(cachos, 1, "Tonto", ronda_especial) is False

# Si el resultado de calzar() es True, el jugador que calza acertó y gana un dado
# si el resultado de calzar() es False, el jugador que calza se equivocó y pierde un dado
@patch('src.juego.dado.random.randint', return_value=3)
def test_resultado_calzar(mock_valor):
    # Configura cachos para test de calzar
    cachos = []
    for i in range(2):
        c = Cacho(3)
        c.agitar()
        cachos.append(c)
    arbitro = ArbitroRonda()

    # Casos básicos de calzar
    assert arbitro.calzar(cachos, 3, "Tren", cachos[0]) is False
    assert arbitro.calzar(cachos, 6, "Tren", cachos[0]) is True
    assert arbitro.calzar(cachos, 2, "Tonto", cachos[0]) is False

    # Modificando dados manualmente
    cachos[0].dados[0].valor = 2
    assert arbitro.calzar(cachos, 4, "Tren", cachos[0]) is False
    assert arbitro.calzar(cachos, 5, "Tren", cachos[0]) is True
    assert arbitro.calzar(cachos, 1, "Tonto", cachos[0]) is True
    assert arbitro.calzar(cachos, 3, "Tonto", cachos[0]) is False

    # Combinando comodines
    cachos[0].dados[1].valor = 1
    assert arbitro.calzar(cachos, 5, "Tren", cachos[0]) is True
    assert arbitro.calzar(cachos, 4, "Tren", cachos[0]) is False
    assert arbitro.calzar(cachos, 2, "Tonto", cachos[0]) is True
    assert arbitro.calzar(cachos, 1, "Tonto", cachos[0]) is False
    assert arbitro.calzar(cachos, 1, "As", cachos[0]) is True

    # Ronda Especial (As no es comodín)
    ronda_especial = True
    assert arbitro.calzar(cachos, 5, "Tren", cachos[0], ronda_especial) is False
    assert arbitro.calzar(cachos, 4, "Tren", cachos[0], ronda_especial) is True
    assert arbitro.calzar(cachos, 2, "Tonto", cachos[0], ronda_especial) is False
    assert arbitro.calzar(cachos, 1, "Tonto", cachos[0], ronda_especial) is True
    assert arbitro.calzar(cachos, 1, "As", cachos[0], ronda_especial) is True


@patch('src.juego.dado.random.randint', return_value=3)
def test_es_valido_calzar(mock_valor):
    # Verifica que calzar inválido lanza excepción
    cachos = []
    for i in range(2):
        c = Cacho(2)
        c.agitar()
        cachos.append(c)
    arbitro = ArbitroRonda()

    with pytest.raises(CalzarInvalido):
        arbitro.calzar(cachos, 2, "Tren", cachos[0])

    # Después de perder un dado, el calzar ahora es válido
    cachos[0].perder_dado()
    assert arbitro.calzar(cachos, 2, "Tren", cachos[0]) is False
    assert arbitro.calzar(cachos, 3, "Tren", cachos[0]) is True
