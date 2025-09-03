import sys
sys.path.append('')

class ContadorPintas:
    def __init__(self):
        pass
    
    def contar(self, pinta, cachos, ronda_especial=False) -> int:
        contador = 0
        for c in cachos:
            for d in c.dados:
                # revisa si corresponde a la pinta o si es comodín
                if d.deno() == pinta:
                    contador += 1
                elif not ronda_especial and d.deno() == "As":
                    contador += 1
        return contador