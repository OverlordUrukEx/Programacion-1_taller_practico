from recursos.modelos.interfaces.volador import Volador


class Avion(Volador):
    def volar(self):
        return "El avión vuela con sus turbinas."