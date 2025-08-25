import sys
sys.path.append('')
from src.juego.cacho import Cacho
from src.juego.dado import Dado

class ContadorPintas:
    def __init__(self):
        pass
    
    def contar(self, pinta, cachos) -> int:
        contador = 0
        for c in cachos:
            for d in c.dados:
                if d.deno() == pinta:
                    contador += 1
        return contador