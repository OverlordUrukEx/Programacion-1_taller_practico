from recursos.modelos.transporte import coche
from recursos.excepciones.excepcionPersonalizada import validar_entrada, validar_anio

# ==========================================================
# EJERCICIO 1: Creación de la Instancia
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
# EJERCICIO 2: Modificación mediante Setters
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

# ==========================================================
# EJERCICIO 3: Constructores
# ==========================================================
print("\n--> Ejercicio 3: Constructores")
coche1 = coche.Coche("Toyota", "Corolla", 2021)
coche2 = coche.Coche("Ford", "Mustang", 2023)
coche3 = coche.Coche("Honda", "Civic", 2019)
coche4 = coche.Coche("Renault", "Sandero", 2015)
coche1.describir()
coche2.describir()
coche3.describir()
coche4.describir()

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

# ==========================================================
# EJERCICIO 7: Clases Abstractas
# ==========================================================
print("\n--> Ejercicio 7: Clases Abstractas")
from recursos.modelos.animales.perro import Perro
from recursos.modelos.animales.gato import Gato
from recursos.modelos.animales.vaca import Vaca
from recursos.modelos.animales.pato import Pato
animales = [Perro(), Gato(), Vaca(), Pato()]
print("--- Sonidos de los animales ---")
for animal in animales:
    animal.hacerSonido()

print("\n" + "|"+ "-"*45 + "|" + "\n" + "|---> Ejercicio 8: Interfaces"  + "\n" + "|" + "-"*45 + "|")
from recursos.modelos.animales.pajaro import Pajaro
from recursos.modelos.transporte.avion import Avion
pajaro = Pajaro()
avion = Avion()
print(pajaro.volar())
print(avion.volar())

# ==========================================================
# EJERCICIO 9: Composición
# ==========================================================
print("\n--> Ejercicio 9: Composicion")
from recursos.modelos.transporte.coche import CocheConMotor
coche1 = CocheConMotor("Lamborghini", "Huracan", 2023, 610, "Gasolina")
coche2 = CocheConMotor("Tesla", "Model S", 2022, 670, "Electrico")
coche3 = CocheConMotor("BMW", "M3", 2021, 503, "Gasolina")
coche4 = CocheConMotor("Toyota", "Prius", 2020, 121, "Hibrido")
coche1.describir()
coche2.describir()
coche3.describir()
coche4.describir()

print("\n" + "|"+ "-"*45 + "|" + "\n" + "|---> Ejercicio 10: Excepciones"  + "\n" + "|" + "-"*45 + "|")
from recursos.modelos.transporte.coche import CocheExcepcion
from recursos.excepciones.excepcionPersonalizada import ExcesoVelocidadException

coche_excepcion = CocheExcepcion("Lamborghini", "Aventador", 2026)
print(coche_excepcion.describir())

try:
    for incremento in [100, 20, 20, 20, 20, 30]:
        print(f"\nIncrementando la velocidad en {incremento} km/h...")
        coche_excepcion.incrementar_velocidad(incremento)
        print(f"Velocidad incrementada exitosamente. Velocidad actual: {coche_excepcion.velocidad_actual} km/h")
except ExcesoVelocidadException as e:
    print("\n" + "|"+ "="*120 + "|" + "\n" + f"|===> Excepción capturada: {e.mensaje} <===|" + "\n" + "|" + "="*120 + "|")
except Exception as e:
    print(f"Error inesperado: {str(e)}")

print(coche_excepcion.describir())
print("\n" + "|"+ "="*90 + "|" + "\n" + "|===> FIN DEL PROGRAMA. Gracias por participar en el taller práctico de Programación 1.<===|"+ "\n" + "|" + "="*90 + "|")
