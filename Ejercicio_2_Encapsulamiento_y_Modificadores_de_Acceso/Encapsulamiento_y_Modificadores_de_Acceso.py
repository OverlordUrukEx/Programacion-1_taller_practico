class Carro:
    def __init__(self, __marca, __modelo, __año): # constructor de la clase
        self.__marca = __marca # atributo de la clase
        self.__modelo = __modelo # atributo de la clase
        self.__año = __año # atributo de la clase
    
    def describir(self): # método de la clase para mostrar la información del carro
        print(f"Marca: {self.__marca}") # muestra la marca del carro
        print(f"Modelo: {self.__modelo}") # muestra el modelo del carro
        print(f"Año: {self.__año}") # muestra el año del carro

    def set_marca(self, marca): # método para establecer la marca del carro
        self.__marca = marca # establece la marca del carro

    def set_modelo(self, modelo): # método para establecer el modelo del carro
        self.__modelo = modelo # establece el modelo del carro

    def set_año(self, año): # método para establecer el año del carro
        self.__año = año # establece el año del carro

        def get_marca(self): # método para obtener la marca del carro
            return self.__marca # devuelve la marca del carro
        
        def get_modelo(self): # método para obtener el modelo del carro
            return self.__modelo # devuelve el modelo del carro
        
        def get_año(self): # método para obtener el año del carro
            return self.__año # devuelve el año del carro