import unittest
from unittest.mock import patch
from src.juego.dado import Dado

@patch('src.juego.dado.random.randint', return_value=2)
def test_dado_valor(mock_valor):
    dado=Dado()
    v_validos=[1,2,3,4,5,6]
    valor=dado.tirar()
    assert valor ==2
    assert valor in v_validos

@patch('src.juego.dado.random.randint', return_value=4)
def test_dado_deno(mock_deno):
    dado=Dado()
    deno_validos=["As","Tonto","Tren","Cuadra","Quina","Sexto"]
    valor=dado.tirar()
    assert dado.deno() =="Cuadra"
    assert dado.deno() in deno_validos