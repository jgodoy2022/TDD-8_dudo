import unittest
from src.juego.dado import Dado

def test_dado_valor():
    dado=Dado()
    v_validos=[1,2,3,4,5,6]
    valor=dado.tirar()
    assert valor in v_validos

def test_dado_deno():
    dado=Dado()
    deno_validos=["As","Tonto","Tren","Cuadra","Quina","Sexto"]
    valor=dado.tirar()
    assert dado.deno() in deno_validos