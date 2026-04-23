class Carro:
    def __init__(self, marca, modelo, año): # constructor de la clase
        self.marca = marca # atributo de la clase
        self.modelo = modelo # atributo de la clase
        self.año = año # atributo de la clase

    def describir(self): # método de la clase para mostrar la información del carro
        print(f"Marca: {self.marca}") # muestra la marca del carro
        print(f"Modelo: {self.modelo}") # muestra el modelo del carro
        print(f"Año: {self.año}") # muestra el año del carro