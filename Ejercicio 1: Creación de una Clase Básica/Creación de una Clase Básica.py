class Carro:
    def __init__(self, marca, modelo, año): # constructor de la clase
        self.marca = marca # atributo de la clase
        self.modelo = modelo # atributo de la clase
        self.año = año # atributo de la clase

    def describir(self): # método de la clase para mostrar la información del carro
        print(f"Marca: {self.marca}") # muestra la marca del carro
        print(f"Modelo: {self.modelo}") # muestra el modelo del carro
        print(f"Año: {self.año}") # muestra el año del carro

# crear una instancia de la clase Carro
mi_carro = Carro("Toyota", "Corolla", 2020)
# crear una segunda instancia de la clase Carro
mi_carro1 = Carro("Honda", "Camry", 2021)
# crear una tercera instancia de la clase Carro
mi_carro2 = Carro("Ford", "Mustang", 2022)


# mostrar la información del carro
mi_carro.describir() # muestra la información del primer carro
mi_carro1.describir() # muestra la información del segundo carro
mi_carro2.describir() # muestra la información del tercer carro 