import sys
sys.path.append('')

class ContadorPintas:
    def __init__(self):
        pass
    
    def contar(self, pinta, cachos) -> int:
        contador = 0
        for c in cachos:
            for d in c.dados:
                if d.deno() == pinta or d.deno() == "As":
                    contador += 1
        return contador