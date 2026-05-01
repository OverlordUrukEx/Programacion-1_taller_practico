class Coche: # definimos la clase Coche
    
    def __init__(self, marca, modelo, anio): # constructor de la clase
        self.marca = marca # guardamos la marca
        self.modelo = modelo # guardamos el modelo
        self.anio = anio # guardamos el anio

    def describir(self): # metodo para mostrar la informacion del coche
        print(f"Marca: {self.marca}") # muestra la marca del coche
        print(f"Modelo: {self.modelo}") # muestra el modelo del coche
        print(f"Año: {self.anio}") # muestra el año del coche


# =========================================================
# EJERCICIO 3: Constructores
# =========================================================
# El constructor __init__ permite darle valores al objeto
# desde el momento en que lo creamos, sin tener que asignarlos despues.
# Aqui creamos varios objetos Coche con diferentes parametros
# para demostrar como funciona el constructor.

print("\n" + "="*40)
print("=== EJERCICIO 3: CONSTRUCTORES ===")

coche1 = Coche("Toyota", "Corolla", 2021) # creamos el primer coche con sus datos
coche2 = Coche("Ford", "Mustang", 2023) # segundo coche con parametros diferentes
coche3 = Coche("Honda", "Civic", 2019) # tercer coche
coche4 = Coche("Renault", "Sandero", 2015) # cuarto coche

# llamamos describir() en cada objeto para verificar que los datos quedaron bien
print("\n--> Estado de los objetos creados con el constructor:")
coche1.describir() # muestra la informacion del primer coche
coche2.describir() # muestra la informacion del segundo coche
coche3.describir() # muestra la informacion del tercer coche
coche4.describir() # muestra la informacion del cuarto coche
