class Vehiculo:
    def __init__(self, velocidad, ruedas):
        self.velocidad = velocidad
        self.ruedas = ruedas

    def acelerar(self):
        return f"El vehículo acelera a {self.velocidad} km/h. Y tiene {self.ruedas} ruedas"