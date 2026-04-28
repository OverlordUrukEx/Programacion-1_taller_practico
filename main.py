from recursos.modelos.transporte import coche

mi_carro_marca = input("Ingrese la marca del carro: ")
mi_carro_modelo = input("Ingrese el modelo del carro: ")
mi_carro_año = int(input("Ingrese el año del carro: "))

mi_carro = coche.Coche(mi_carro_marca, mi_carro_modelo, mi_carro_año)
mi_carro1 = coche.Coche("Honda", "Camry", 2021)
mi_carro2 = coche.Coche("Ford", "Mustang", 2022)

mi_carro.describir()
mi_carro1.describir()
mi_carro2.describir()