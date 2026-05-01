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

print("\n" + "|"+ "-"*30 + "|" + "\n" + "|---> Ejercicio 4: Herencia"  + "\n" + "|" + "-"*30 + "|")
from recursos.modelos.transporte.carro import Carro
from recursos.modelos.transporte.bicicleta import Bicicleta
carro1 = Carro(120, 4, "Todoterreno", "Diesel")
carro2 = Carro(150, 4, "Deportivo", "Gasolina")
bicicleta1 = Bicicleta(30, 2, "Trek", "Montaña")
bicicleta2 = Bicicleta(25, 2, "Giant", "Urbana")
print(carro1.describir_carro())
print(carro2.describir_carro())
print(bicicleta1.describir_bicicleta())
print(bicicleta2.describir_bicicleta())

print("\n" + "|"+ "-"*45 + "|" + "\n" + "|---> Ejercicio 5: Sobrescritura de Métodos"  + "\n" + "|" + "-"*45 + "|")
print(carro1.acelerar())
print(carro2.acelerar())
print(carro1.propiedades())
print(carro2.propiedades())
print(bicicleta1.acelerar())
print(bicicleta2.acelerar())
print(bicicleta1.propiedades())
print(bicicleta2.propiedades())

print("\n" + "|"+ "-"*30 + "|" + "\n" + "|---> Ejercicio 6: Polimorfismo"  + "\n" + "|" + "-"*30 + "|")
vehiculos = [carro1, carro2, bicicleta1, bicicleta2]
for v in vehiculos:
    print(v.acelerar())
    print(v.propiedades())

print("\n" + "|"+ "-"*30 + "|" + "\n" + "|---> Ejercicio 8: Interfaces"  + "\n" + "|" + "-"*30 + "|")
from recursos.modelos.animales.pajaro import Pajaro
from recursos.modelos.transporte.avion import Avion
pajaro = Pajaro()
avion = Avion()
print(pajaro.volar())
print(avion.volar())