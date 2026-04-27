import Creacion_de_una_Clase_Básica

# crear una instancia de la clase Carro
mi_carro_marca = input("Ingrese la marca del carro: ")
mi_carro_modelo = input("Ingrese el modelo del carro: ")
mi_carro_año = int(input("Ingrese el año del carro: ")) 
mi_carro = Creacion_de_una_Clase_Básica.Carro(mi_carro_marca, mi_carro_modelo, mi_carro_año)
# crear una segunda instancia de la clase Carro
mi_carro1 = Creacion_de_una_Clase_Básica.Carro("Honda", "Camry", 2021)
# crear una tercera instancia de la clase Carro
mi_carro2 = Creacion_de_una_Clase_Básica.Carro("Ford", "Mustang", 2022)

# mostrar la información del carro
mi_carro.describir() # muestra la información del primer carro
mi_carro1.describir() # muestra la información del segundo carro
mi_carro2.describir() # muestra la información del tercer carro