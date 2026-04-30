from recursos.modelos.transporte import coche
from recursos.excepciones.excepcionPersonalizada import validar_entrada, validar_anio

# ==========================================================
# EJERCICIO 1: Creación de la Instancia [cite: 1]
# ==========================================================
print("=== EJERCICIO 1: CREACIÓN DE OBJETO ===")
marca_ini = validar_entrada("Ingrese marca inicial: ")
mod_ini = validar_entrada("Ingrese modelo inicial: ")
anio_ini = validar_anio("Ingrese año inicial: ")

# Creamos el objeto con los datos capturados [cite: 4]
mi_carro = coche.Coche(marca_ini, mod_ini, anio_ini)

print("\n--> Estado del objeto tras Ejercicio 1:")
mi_carro.describir()

# ==========================================================
# EJERCICIO 2: Modificación mediante Setters [cite: 6]
# ==========================================================
print("\n" + "="*40) # Separador visual para diferenciar los ejercicios
print("=== EJERCICIO 2: ACTUALIZACIÓN (SETTERS) ===")
print("Vamos a modificar el objeto existente...")

# Capturamos nuevos datos para demostrar los métodos SET 
nueva_marca = validar_entrada("Ingrese la NUEVA marca: ")
nuevo_mod = validar_entrada("Ingrese el NUEVO modelo: ")
nuevo_anio = validar_anio("Ingrese el NUEVO año: ")

# Aplicamos los cambios al objeto original 
mi_carro.setMarca(nueva_marca)
mi_carro.setModelo(nuevo_mod)
mi_carro.setAnio(nuevo_anio)

print("\n--> Estado del objeto tras Ejercicio 2 (Actualizado):")
# Verificamos los cambios usando los Getters o el método describir 
print(f"Confirmación de marca vía Getter: {mi_carro.getMarca()}")
mi_carro.describir()

print("\nEjercicio 8: Interfaces")
from recursos.modelos.interfaces.volador import Pajaro, Avion
pajaro = Pajaro()
avion = Avion()
print(pajaro.volar())
print(avion.volar())