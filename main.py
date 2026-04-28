from recursos.modelos.transporte import coche

mi_carro_marca = input("Ingrese la marca del carro: ")
mi_carro_modelo = input("Ingrese el modelo del carro: ")
mi_carro_año = int(input("Ingrese el año del carro: "))

mi_carro = coche.Coche(mi_carro_marca, mi_carro_modelo, mi_carro_año)
mi_carro1 = coche.Coche("Honda", "Camry", 2021)
mi_carro2 = coche.Coche("Ford", "Mustang", 2022)

print("\n--> Instancia 1")
mi_carro.describir()
print("\n--> Instancia 2")
mi_carro1.describir()
print("\n--> Instancia 3")
mi_carro2.describir()