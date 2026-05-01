from recursos.modelos.transporte.vehiculo import Vehiculo 

class Carro(Vehiculo):
    def __init__(self, velocidad, ruedas, tipo_carro, tipo_combustible):
        super().__init__(velocidad, ruedas)
        self.tipo_carro = tipo_carro
        self.tipo_combustible = tipo_combustible

    def describir_carro(self):
        return f"El carro es un {self.tipo_carro} que utiliza {self.tipo_combustible} como combustible."
    
    def acelerar(self):
        return f"El carro acelera apretando el acelerador a {self.velocidad} km/h."
    
    def propiedades(self):
        return f"El carro tiene {self.ruedas} ruedas."