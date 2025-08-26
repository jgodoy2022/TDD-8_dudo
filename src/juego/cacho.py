from src.juego.dado import Dado

class Cacho:
    
    def cantidad_dados(self):
        return len(self.dados)

    # Inicializa el cacho con 5 dados
    def __init__(self, cantidad_dados=5):
        self.dados = []
        self.dados_extra = 0
        for _ in range(cantidad_dados):
            self.dados.append(Dado())

    # Emplea la funcion tirar para cada dado
    def agitar(self):
        for dado in self.dados:
            dado.tirar()
    # Funcion para eliminar un dado
    def perder_dado(self):
        if len(self.dados) > 0 and self.dados_extra == 0:
            self.dados.pop()
        elif self.dados_extra > 0:
            self.dados_extra -= 1

    # Funcion para ganar dado
    def ganar_dado(self):
        if len(self.dados) == 5:
            self.dados_extra += 1

        else:
            dado=Dado()
            dado.tirar()
            self.dados.append(dado)
