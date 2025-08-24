import pytest
from src.juego.validador_apuesta import Apuesta, ValidadorApuesta


@pytest.fixture
def validador():
    return ValidadorApuesta()


def test_primera_apuesta_valida(validador):
    assert validador.es_valida(Apuesta(2, 3)) is True  
    assert validador.apuesta_actual.cantidad == 2
    assert validador.apuesta_actual.pinta == 3


def test_no_se_puede_iniciar_con_ases(validador):
    assert validador.es_valida(Apuesta(2, 1)) is False  
    assert validador.es_valida(Apuesta(1, 1)) is True   


def test_apuesta_superior_por_cantidad(validador):
    validador.es_valida(Apuesta(2, 3))  
    assert validador.es_valida(Apuesta(3, 2)) is True   


def test_apuesta_superior_por_pinta(validador):
    validador.es_valida(Apuesta(2, 3))   
    assert validador.es_valida(Apuesta(2, 4)) is True   
    assert validador.es_valida(Apuesta(2, 2)) is False  


def test_cambio_a_ases(validador):
    validador.es_valida(Apuesta(5, 6))   
    assert validador.es_valida(Apuesta(2, 1)) is False  
    assert validador.es_valida(Apuesta(3, 1)) is True   


def test_cambio_desde_ases(validador):
    validador.es_valida(Apuesta(2, 1))   
    assert validador.es_valida(Apuesta(4, 6)) is False  
    assert validador.es_valida(Apuesta(5, 6)) is True   
