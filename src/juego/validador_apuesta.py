class Apuesta:
    def __init__(self, cantidad, pinta):
        self.cantidad = cantidad
        self.pinta = pinta  

    def __repr__(self):
        return f"{self.cantidad} de {self.pinta}"

class ValidadorApuesta:
    def __init__(self):
        self.apuesta_actual = None

    def es_valida(self, nueva_apuesta: Apuesta, ronda_especial=False) -> bool:
        # Si es la primera apuesta
        if self.apuesta_actual is None:
            if not ronda_especial and nueva_apuesta.pinta == 1 and nueva_apuesta.cantidad > 1:
                # No se puede partir con Ases salvo si hay 1 dado
                return False
            self.apuesta_actual = nueva_apuesta
            return True

        actual = self.apuesta_actual

        if ronda_especial:
            # En ronda especial, los Ases pierden privilegio y se aplican reglas normales
            if nueva_apuesta.cantidad < actual.cantidad:
                return False
            if nueva_apuesta.cantidad == actual.cantidad and nueva_apuesta.pinta <= actual.pinta:
                return False
            self.apuesta_actual = nueva_apuesta
            return True

        # Reglas normales fuera de ronda especial
        if nueva_apuesta.pinta == 1 and actual.pinta != 1:
            limite = (actual.cantidad // 2) + (1 if actual.cantidad % 2 != 0 else 0)
            if nueva_apuesta.cantidad < limite:
                return False

        elif actual.pinta == 1 and nueva_apuesta.pinta != 1:
            limite = actual.cantidad * 2 + 1
            if nueva_apuesta.cantidad < limite:
                return False

        else:
            if nueva_apuesta.cantidad < actual.cantidad:
                return False
            if nueva_apuesta.cantidad == actual.cantidad and nueva_apuesta.pinta <= actual.pinta:
                return False

        self.apuesta_actual = nueva_apuesta
        return True
