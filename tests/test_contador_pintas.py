import pytest
import sys
sys.path.append('')
from src.juego.contador_pintas import ContadorPintas
from src.juego.cacho import Cacho
from src.juego.dado import Dado
from unittest.mock import patch


@patch('src.juego.dado.random.randint', return_value=2)
def test_contar_pintas(mock_valor):
    # Todos los dados salen con valor 2 ("Tonto")
    cacho1 = Cacho(3)
    cacho1.agitar()
    cacho2 = Cacho(2)
    cacho2.agitar()
    cachos = [cacho1, cacho2]
    con = ContadorPintas()

    # Los 5 dados deberían ser "Tonto"
    assert con.contar("Tonto", cachos) == 5

    # Cambiamos algunos valores manualmente
    cacho1.dados[0].valor = 3   # "Tren"
    cacho1.dados[2].valor = 5   # "Quina"
    cacho2.dados[1].valor = 3   # "Tren"

    # Recuento actualizado
    assert con.contar("Tonto", cachos) == 2
    assert con.contar("Tren", cachos) == 2
    assert con.contar("Quina", cachos) == 1
    assert con.contar("Cuadra", cachos) == 0


@patch('src.juego.dado.random.randint', return_value=1)
def test_contar_comodin(mock_valor):
    # Todos los dados salen con valor 1 ("As"), que cuenta como comodín
    cacho1 = Cacho(2)
    cacho1.agitar()
    cacho2 = Cacho(2)
    cacho2.agitar()
    cachos = [cacho1, cacho2]
    con = ContadorPintas()

    # Los Ases cuentan para cualquier pinta
    assert con.contar("As", cachos) == 4
    assert con.contar("Tonto", cachos) == 4
    assert con.contar("Tren", cachos) == 4
    assert con.contar("Cuadra", cachos) == 4
    assert con.contar("Quina", cachos) == 4
    assert con.contar("Sexto", cachos) == 4

    # Cambiamos algunos valores manualmente
    cacho1.dados[0].valor = 3   # "Tren"
    cacho1.dados[1].valor = 5   # "Quina"
    cacho2.dados[1].valor = 3   # "Tren"

    # Recuento actualizado (considerando comodines)
    assert con.contar("As", cachos) == 1
    assert con.contar("Tren", cachos) == 3
    assert con.contar("Quina", cachos) == 2

@patch('src.juego.dado.random.randint', return_value=1)
def test_contar_en_ronda_especial(mock_valor):
    # Todos los dados salen con valor 1 ("As"), que cuenta como comodín
    cacho1 = Cacho(2)
    cacho1.agitar()
    cacho2 = Cacho(2)
    cacho2.agitar()
    cachos = [cacho1, cacho2]
    con = ContadorPintas()

    # indica si es ronda especial o no
    ronda_especial = True

    # Los Ases cuentan para cualquier pinta
    assert con.contar("As", cachos, ronda_especial) == 4
    assert con.contar("Tonto", cachos, ronda_especial) == 0
    assert con.contar("Tren", cachos, ronda_especial) == 0
    assert con.contar("Cuadra", cachos, ronda_especial) == 0
    assert con.contar("Quina", cachos, ronda_especial) == 0
    assert con.contar("Sexto", cachos, ronda_especial) == 0

    # Cambiamos algunos valores manualmente
    cacho1.dados[0].valor = 3   # "Tren"
    cacho1.dados[1].valor = 5   # "Quina"
    cacho2.dados[1].valor = 3   # "Tren"

    # Recuento actualizado (considerando comodines)
    assert con.contar("As", cachos) == 1
    assert con.contar("Tren", cachos) == 2
    assert con.contar("Quina", cachos) == 1