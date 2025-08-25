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
