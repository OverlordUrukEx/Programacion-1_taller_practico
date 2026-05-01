# =========================================================
# EJERCICIO 9: Composición
# =========================================================

# La composicion es cuando una clase tiene dentro un objeto de otra clase.
# En este caso, Coche tiene un Motor adentro.

class Motor: # clase Motor con sus atributos
    def __init__(self, potencia, tipo):
        self.potencia = potencia # potencia del motor en caballos de fuerza
        self.tipo = tipo # tipo de motor, por ejemplo gasolina o electrico

    def describir(self):
        print(f"  Motor: {self.tipo}, {self.potencia} HP") # muestra los detalles del motor


class Coche: # clase Coche que contiene un objeto Motor
    def __init__(self, marca, modelo, potencia, tipo):
        self.marca = marca # marca del coche
        self.modelo = modelo # modelo del coche
        self.motor = Motor(potencia, tipo) # creamos el motor dentro del coche

    def describir(self): # describe el coche incluyendo los detalles del motor
        print(f"Coche: {self.marca} {self.modelo}") # muestra marca y modelo
        self.motor.describir() # llama al describir del motor
        print("-" * 25)


# creamos algunos coches con sus motores
coche1 = Coche("Lamborghini", "Huracan", 610, "Gasolina")
coche2 = Coche("Tesla", "Model S", 670, "Electrico")
coche3 = Coche("BMW", "M3", 503, "Gasolina")

print("--- Coches y sus motores ---")
coche1.describir()
coche2.describir()
coche3.describir()