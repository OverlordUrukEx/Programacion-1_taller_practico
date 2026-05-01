from abc import ABC, abstractmethod # importamos las herramientas para crear clases abstractas

# =========================================================
# EJERCICIO 7: Clases Abstractas
# =========================================================
# Una clase abstracta es una plantilla que no se puede instanciar sola, obliga a las clases hijas a implementar sus metodos abstractos.

class Animal(ABC): # clase abstracta base
    @abstractmethod
    def hacerSonido(self): # las clases hijas estan obligadas a definir este metodo
        pass


class Perro(Animal): # Perro hereda de Animal
    def hacerSonido(self):
        print("Perro: ¡Guau!") # sonido del perro

class Gato(Animal): # Gato hereda de Animal
    def hacerSonido(self):
        print("Gato: ¡Miau!") # sonido del gato


class Vaca(Animal): # Vaca hereda de Animal
    def hacerSonido(self):
        print("Vaca: ¡Muuu!") # sonido de la vaca


class Pato(Animal): # Pato hereda de Animal
    def hacerSonido(self):
        print("Pato: ¡Cuac!") # sonido del pato


# creamos la lista con varios animales
animales = [Perro(), Gato(), Vaca(), Pato()]

print("--- Sonidos de los animales ---")
for animal in animales: # recorremos la lista y llamamos hacerSonido() en cada uno
    animal.hacerSonido()