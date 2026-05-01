from recursos.modelos.transporte.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, ruedas, marca, tipo_bicicleta):
        super().__init__(velocidad, ruedas)
        self.marca = marca
        self.tipo_bicicleta = tipo_bicicleta

    def describir_bicicleta(self):
        return f"La bicicleta es una {self.tipo_bicicleta} de la marca {self.marca} que acelera a {self.velocidad} km/h y tiene {self.ruedas} ruedas."