"""
Módulo de utilidades para validación de datos de entrada.
"""
# Función para validar que la entrada del usuario no esté vacía. Recibe un mensaje como parámetro para mostrar al usuario.
def validar_entrada(mensaje): 
    """Valida que la cadena de texto no esté vacía."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("-> Error: Este campo es obligatorio.")
# Función para validar que el año ingresado sea un número entero dentro de un rango lógico para vehículos. Recibe un mensaje como parámetro para mostrar al usuario.
def validar_anio(mensaje):
    """Valida que el año sea un entero dentro de un rango histórico válido."""
    while True:
        try:
            anio = int(input(mensaje))
            if 1886 <= anio <= 2026:
                return anio
            print("-> Error: Ingrese un año válido (1886-2026).")
        except ValueError:
            print("-> Error: Debe ser un número entero.")