from src.juego.dado import Dado

class Cacho:
    
    def cantidad_dados(self):
        return len(self.dados)

    # Inicializa el cacho con 5 dados
    def __init__(self, cantidad_dados=5):
        self.dados = []
        self.dados_extra = 0
        self.visible = True
        self.visible_demas = False
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

    # Funcion mostrar cacho
    def cambiar_mostrar(self):
        self.visible = not self.visible

    # Funcion mostrar resto de cachos
    def cambiar_mostrar_demas(self):
        self.visible_demas = not self.visible_demas