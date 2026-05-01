class Vehiculo:
    def __init__(self, velocidad, ruedas):
        self.velocidad = velocidad
        self.ruedas = ruedas

    def acelerar(self):
        return f"El vehículo acelera a {self.velocidad} km/h."
    
    def propiedades(self):
        return f"El vehículo tiene {self.ruedas} ruedas."