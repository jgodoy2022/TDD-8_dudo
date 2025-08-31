import pytest
import sys
sys.path.append('')
from src.juego.contador_pintas import ContadorPintas
from src.juego.cacho import Cacho
from src.juego.dado import Dado
from unittest.mock import patch

@patch('src.juego.dado.random.randint', return_value = 2)
def test_contar_pintas(mock_valor):
    cacho1 = Cacho(3)
    cacho1.agitar()
    cacho2 = Cacho(2)
    cacho2.agitar()
    cachos = []
    cachos.append(cacho1)
    cachos.append(cacho2)
    con = ContadorPintas()

    assert con.contar("Tonto", cachos) == 5

    cacho1.dados[0].valor = 3
    cacho1.dados[2].valor = 5
    cacho2.dados[1].valor = 3

    assert con.contar("Tonto", cachos) == 2
    assert con.contar("Tren", cachos) == 2
    assert con.contar("Quina", cachos) == 1
    assert con.contar("Cuadra", cachos) == 0

@patch('src.juego.dado.random.randint', return_value = 1)
def test_contar_comodin(mock_valor):
    cacho1 = Cacho(2)
    cacho1.agitar()
    cacho2 = Cacho(2)
    cacho2.agitar()
    cachos = []
    cachos.append(cacho1)
    cachos.append(cacho2)
    con = ContadorPintas()

    assert con.contar("As", cachos) == 4
    assert con.contar("Tonto", cachos) == 4
    assert con.contar("Tren", cachos) == 4
    assert con.contar("Cuadra", cachos) == 4
    assert con.contar("Quina", cachos) == 4
    assert con.contar("Sexto", cachos) == 4

    cacho1.dados[0].valor = 3
    cacho1.dados[1].valor = 5
    cacho2.dados[1].valor = 3

    assert con.contar("As", cachos) == 1
    assert con.contar("Tren", cachos) == 3
    assert con.contar("Quina", cachos) == 2