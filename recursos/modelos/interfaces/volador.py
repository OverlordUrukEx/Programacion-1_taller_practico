from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pajaro(Volador):
    def volar(self):
        print("El pájaro vuela con sus alas.")

class Avion(Volador):
    def volar(self):
        print("El avión vuela con sus turbinas.")