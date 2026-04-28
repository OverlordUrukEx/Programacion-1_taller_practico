class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def set_año(self, año):
        self.__año = año

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo
    
    def get_año(self):
         return self.__año