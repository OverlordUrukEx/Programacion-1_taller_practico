class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir(self):
        return f"Motor: {self.tipo}, {self.potencia} HP"
