from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dados = []
        for _ in range(5):
            self.dados.append(Dado())


