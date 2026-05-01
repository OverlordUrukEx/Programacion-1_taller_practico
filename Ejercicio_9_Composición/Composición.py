# 1. Primero definimos la pieza pequeña: El Motor
class Motor:
    def __init__(self, potencia, tipo):
        # Guardamos las características básicas del motor
        self.potencia = potencia
        self.tipo = tipo

    def describir_motor(self):
        # Un método para que el motor diga sus características
        return f"Motor {self.tipo} de {self.potencia} CV"

# 2. Definimos la clase principal: El Coche
class Coche:
    def __init__(self, marca, modelo, motor):
        # Aquí está la COMPOSICIÓN:
        # El coche no solo recibe datos, recibe un OBJETO Motor completo.
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # <-- Esta variable guarda el objeto Motor que recibimos

    def describir(self):
        # Al pedirle al motor que se describa, usamos el objeto motor que guardamos arriba
        info_motor = self.motor.describir_motor()
        print(f"Coche: {self.marca} {self.modelo} | {info_motor}")

# --- Programa Principal ---

# Primero creamos el motor (es como armar la pieza por separado)
mi_motor = Motor(150, "Gasolina")

# Ahora creamos el coche y le "metemos" el motor dentro
mi_coche = Coche("Toyota", "Corolla", mi_motor)

# Verificamos
print("--- Resultado de la Composición ---")
mi_coche.describir()