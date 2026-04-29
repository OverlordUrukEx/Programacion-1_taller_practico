class Coche: # Definición de la clase Coche, que representa un vehículo con atributos y métodos relacionados.
    def __init__(self, marca, modelo, anio): # Constructor de la clase Coche, que se llama automáticamente al crear una instancia de esta clase. Recibe tres parámetros: marca, modelo y año, que son necesarios para crear un objeto de tipo Coche.
        # Atributos públicos: La forma más básica y simple de iniciar
        self.marca = marca # Aunque la marca es un dato importante, lo dejamos como público para simplificar el acceso a esta información. En un caso real, podríamos querer protegerlo con validaciones adicionales, pero para este ejemplo, lo mantenemos simple.
        self.modelo = modelo # Aunque el modelo es un dato importante, lo dejamos como público para simplificar el acceso a esta información. En un caso real, podríamos querer protegerlo con validaciones adicionales, pero para este ejemplo, lo mantenemos simple.
        self.anio = anio # Aunque el año es un dato importante, lo dejamos como público para simplificar el acceso a esta información. En un caso real, podríamos querer protegerlo con validaciones adicionales, pero para este ejemplo, lo mantenemos simple.

# --- Getters y Setters para MARCA ---
    def getMarca(self): # El método getMarca() es un getter que permite acceder al valor del atributo privado __marca desde fuera de la clase. Devuelve el valor actual de la marca del coche.
        return self.__marca  # El getter getMarca() devuelve el valor del atributo privado __marca. Esto permite que otras partes del programa puedan obtener la marca del coche sin acceder directamente al atributo privado, lo que es una buena práctica de encapsulación.

    def setMarca(self, nueva_marca): # El método setMarca(nueva_marca) es un setter que permite modificar el valor del atributo privado __marca desde fuera de la clase. Recibe un nuevo valor para la marca y lo asigna al atributo __marca.
        self.__marca = nueva_marca # El setter setMarca() asigna el nuevo valor de la marca al atributo privado __marca. Esto permite controlar cómo se modifica la marca del coche, y podríamos agregar validaciones adicionales aquí si quisiéramos asegurarnos de que la marca sea válida (por ejemplo, no vacía o dentro de una lista de marcas permitidas). En este ejemplo, simplemente asignamos el nuevo valor sin validaciones para mantenerlo simple.

    # --- Getters y Setters para MODELO ---
    def getModelo(self): # El método getModelo() es un getter que permite acceder al valor del atributo privado __modelo desde fuera de la clase. Devuelve el valor actual del modelo del coche.
        return self.__modelo # El getter getModelo() devuelve el valor del atributo privado __modelo. Esto permite que otras partes del programa puedan obtener el modelo del coche sin acceder directamente al atributo privado, lo que es una buena práctica de encapsulación.

    def setModelo(self, nuevo_modelo): # El método setModelo(nuevo_modelo) es un setter que permite modificar el valor del atributo privado __modelo desde fuera de la clase. Recibe un nuevo valor para el modelo y lo asigna al atributo __modelo.
        self.__modelo = nuevo_modelo # El setter setModelo() asigna el nuevo valor del modelo al atributo privado __modelo. Esto permite controlar cómo se modifica el modelo del coche, y podríamos agregar validaciones adicionales aquí si quisiéramos asegurarnos de que el modelo sea válido (por ejemplo, no vacío o dentro de una lista de modelos permitidos). En este ejemplo, simplemente asignamos el nuevo valor sin validaciones para mantenerlo simple.

    # --- Getters y Setters para AÑO ---
    def getAnio(self): # El método getAnio() es un getter que permite acceder al valor del atributo privado __anio desde fuera de la clase. Devuelve el valor actual del año del coche.
        return self.__anio # El getter getAnio() devuelve el valor del atributo privado __anio. Esto permite que otras partes del programa puedan obtener el año del coche sin acceder directamente al atributo privado, lo que es una buena práctica de encapsulación.

    def setAnio(self, nuevo_anio): # El método setAnio(nuevo_anio) es un setter que permite modificar el valor del atributo privado __anio desde fuera de la clase. Recibe un nuevo valor para el año y lo asigna al atributo __anio.
        self.__anio = nuevo_anio # El setter setAnio() asigna el nuevo valor del año al atributo privado __anio. Esto permite controlar cómo se modifica el año del coche, y podríamos agregar validaciones adicionales aquí si quisiéramos asegurarnos de que el año sea válido (por ejemplo, dentro de un rango lógico). En este ejemplo, simplemente asignamos el nuevo valor sin validaciones para mantenerlo simple.

    # --- Método de Acción ---
    def describir(self):
        # Internamente, la clase sí puede acceder a sus atributos privados
        print(f"Marca: {self.__marca}") # El método describir() muestra la información del coche en la consola. Accede a los atributos privados __marca, __modelo y __anio para mostrar su valor. Esto demuestra que dentro de la clase, podemos acceder a los atributos privados sin problemas, lo que es una parte fundamental de la encapsulación en la programación orientada a objetos.
        print(f"Modelo: {self.__modelo}") # El método describir() muestra la información del coche en la consola. Accede a los atributos privados __marca, __modelo y __anio para mostrar su valor. Esto demuestra que dentro de la clase, podemos acceder a los atributos privados sin problemas, lo que es una parte fundamental de la encapsulación en la programación orientada a objetos.
        print(f"Año: {self.__anio}") # El método describir() muestra la información del coche en la consola. Accede a los atributos privados __marca, __modelo y __anio para mostrar su valor. Esto demuestra que dentro de la clase, podemos acceder a los atributos privados sin problemas, lo que es una parte fundamental de la encapsulación en la programación orientada a objetos.
