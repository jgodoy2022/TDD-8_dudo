from src.juego.dado import Dado

class Cacho:

    # Inicializa el cacho con 5 dados
    def __init__(self):
        self.dados = []
        for _ in range(5):
            self.dados.append(Dado())

    # Emplea la funcion tirar para cada dado
    def agitar(self):
        for dado in self.dados:
            dado.tirar()


