from recursos.modelos.transporte import coche

print("--- REGISTRO DE VEHÍCULO ---")

# 1. Validación de la Marca (No puede estar vacía)
while True: # Este ciclo se repetirá hasta que el usuario ingrese una marca válida (no vacía).
    mi_carro_marca = input("Ingrese la marca del carro: ").strip() # .strip() elimina espacios al inicio y al final
    if mi_carro_marca != "":
        break # Si el usuario ingresa una marca válida, salimos del ciclo y continuamos con la validación del modelo.
    print("-> Error: La marca no puede estar vacía.") # Si el usuario no ingresa nada, el programa no avanza y muestra un mensaje de error.

# 2. Validación del Modelo (No puede estar vacío)
while True: # Este ciclo se repetirá hasta que el usuario ingrese un modelo válido (no vacío).
    mi_carro_modelo = input("Ingrese el modelo del carro: ").strip() # .strip() elimina espacios al inicio y al final
    if mi_carro_modelo != "":
        break # Si el usuario ingresa un modelo válido, salimos del ciclo y continuamos con la validación del año.
    print("-> Error: El modelo no puede estar vacío.") # Si el usuario no ingresa nada, el programa no avanza y muestra un mensaje de error.

# 3. Validación del Año (Debe ser un número entero válido)
while True: # Este ciclo se repetirá hasta que el usuario ingrese un año válido (un número entero dentro de un rango lógico).
    try:
        # Intentamos convertir lo que el usuario escribe a un número entero
        mi_carro_anio = int(input("Ingrese el año del carro: ")) # Si el usuario ingresa algo que no se puede convertir a entero, el programa no avanza y muestra un mensaje de error crítico.
        
        # Validamos que el año tenga sentido lógico
        if 1886 <= mi_carro_anio <= 2026: # El primer automóvil fue inventado en 1886, y 2026 es un año futuro cercano, por lo que este rango es razonable para un año de fabricación de un carro.
            break # Si el año es válido, salimos del ciclo y continuamos con la creación del objeto.
        else:
            print("-> Error: Ingrese un año lógico (ej. entre 1886 y 2026).") # Si el usuario ingresa un año fuera de rango, el programa no avanza y muestra un mensaje de error.
    except ValueError: 
        # Si el usuario escribe letras, el programa no colapsa, entra aquí:
        print("-> Error Crítico: El año debe ser un número entero.") # Si el usuario ingresa algo que no se puede convertir a entero, el programa no avanza y muestra un mensaje de error crítico.

# Instanciamos el objeto con los datos ya validados
mi_carro = coche.Coche(mi_carro_marca, mi_carro_modelo, mi_carro_anio)

print("\n--> Instancia 1") # Mostramos la información del carro utilizando el método describir()
mi_carro.describir() # Este método muestra la marca, modelo y año del carro en la consola.

print("--- DEMOSTRACIÓN DE ENCAPSULAMIENTO ---")

# 1. Instanciamos el objeto con datos iniciales
mi_carro = coche.Coche("Toyota", "Corolla", 2020) # Creamos un nuevo objeto de tipo Coche con marca "Toyota", modelo "Corolla" y año 2020. Estos datos se pasan al constructor de la clase Coche, que los asigna a los atributos privados del objeto.

print("\n--> Estado Inicial:") # Mostramos la información del carro utilizando el método describir() para verificar que los datos se han asignado correctamente.
mi_carro.describir() # Este método muestra la marca, modelo y año del carro en la consola. Internamente, accede a los atributos privados __marca, __modelo y __anio para mostrar su valor. Esto demuestra que dentro de la clase, podemos acceder a los atributos privados sin problemas, lo que es una parte fundamental de la encapsulación en la programación orientada a objetos.

# 2. Usamos los métodos SET para modificar los atributos privados 
print("\nActualizando datos del vehículo...") # Aquí estamos utilizando los métodos setMarca(), setModelo() y setAnio() para modificar los valores de los atributos privados del objeto mi_carro. Estos métodos permiten controlar cómo se modifican los datos del carro, y podríamos agregar validaciones adicionales dentro de estos métodos si quisiéramos asegurarnos de que los nuevos valores sean válidos. En este ejemplo, simplemente asignamos los nuevos valores sin validaciones para mantenerlo simple.
mi_carro.setMarca("Honda") # El método setMarca() asigna el nuevo valor "Honda" al atributo privado __marca del objeto mi_carro. Esto demuestra cómo podemos modificar un atributo privado desde fuera de la clase utilizando un setter, lo que es una parte clave de la encapsulación en la programación orientada a objetos.
mi_carro.setModelo("Civic") # El método setModelo() asigna el nuevo valor "Civic" al atributo privado __modelo del objeto mi_carro. Esto demuestra cómo podemos modificar un atributo privado desde fuera de la clase utilizando un setter, lo que es una parte clave de la encapsulación en la programación orientada a objetos.
mi_carro.setAnio(2024) # El método setAnio() asigna el nuevo valor 2024 al atributo privado __anio del objeto mi_carro. Esto demuestra cómo podemos modificar un atributo privado desde fuera de la clase utilizando un setter, lo que es una parte clave de la encapsulación en la programación orientada a objetos.

# 3. Usamos los métodos GET para acceder a un atributo específico 
print(f"\nLa nueva marca registrada es: {mi_carro.getMarca()}") # El método getMarca() devuelve el valor del atributo privado __marca del objeto mi_carro, que ahora es "Honda". Esto demuestra cómo podemos acceder a un atributo privado desde fuera de la clase utilizando un getter, lo que es una parte clave de la encapsulación en la programación orientada a objetos.

print("\n--> Estado Modificado:")
mi_carro.describir()