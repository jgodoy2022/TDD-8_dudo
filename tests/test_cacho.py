from src.juego.cacho import Cacho

def test_cacho_inicio():
    cacho = Cacho()
    assert len(cacho.dados) == 5