class Apuesta:
    def __init__(self, cantidad, pinta):
        self.cantidad = cantidad
        self.pinta = pinta  

    def __repr__(self):
        return f"{self.cantidad} de {self.pinta}"


class ValidadorApuesta:
    def __init__(self):
        self.apuesta_actual = None

    def es_valida(self, nueva_apuesta: Apuesta) -> bool:
        # Si es la primera apuesta
        if self.apuesta_actual is None:
            # No se puede partir con Ases (excepto con 1 dado)
            if nueva_apuesta.pinta == 1 and nueva_apuesta.cantidad > 1:
                return False
            self.apuesta_actual = nueva_apuesta
            return True

        # Reglas normales (misma pinta o superior)
        actual = self.apuesta_actual

        if nueva_apuesta.pinta == 1 and actual.pinta != 1:
            # Cambio a Ases: cantidad = ceil(actual.cantidad / 2)
            limite = (actual.cantidad // 2) + (1 if actual.cantidad % 2 != 0 else 0)
            if nueva_apuesta.cantidad < limite:
                return False

        elif actual.pinta == 1 and nueva_apuesta.pinta != 1:
            # Cambio desde Ases: cantidad = actual.cantidad * 2 + 1
            limite = actual.cantidad * 2 + 1
            if nueva_apuesta.cantidad < limite:
                return False

        else:
            # Apuesta normal (misma pinta o superior)
            if nueva_apuesta.cantidad < actual.cantidad:
                return False
            if nueva_apuesta.cantidad == actual.cantidad and nueva_apuesta.pinta <= actual.pinta:
                return False

        self.apuesta_actual = nueva_apuesta
        return True
