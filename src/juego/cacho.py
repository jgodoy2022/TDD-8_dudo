from src.juego.dado import Dado

class Cacho:

    # Inicializa el cacho con 5 dados
    def __init__(self, cantidad_dados=5):
        self.dados = []
        for _ in range(cantidad_dados):
            self.dados.append(Dado())

    # Emplea la funcion tirar para cada dado
    def agitar(self):
        for dado in self.dados:
            dado.tirar()
    # Funcion para eliminar un dado
    def perder_dado(self):
        self.dados.pop()

    def ganar_dado(self):
        if len(self.dados) == 5:
            pass

        else:
            dado=Dado()
            dado.tirar()
            self.dados.append(dado)
