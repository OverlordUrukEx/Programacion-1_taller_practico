# Programación I - Taller Práctico: Modelamiento de Clases

Este repositorio contiene la solución al taller 1 de modelamiento de objetos en Python.

| Integrante | Fichero                                                                                          | Ejercicios        |
|------------|--------------------------------------------------------------------------------------------------|-------------------|
| Johan      | coche.py, excepcionPersonalizada.py                                                              | 1, 2, 10          |
| Isabella   | animal.py, perro.py, gato.py, pato.py, vaca.py, motor.py                                         | 3, 7, 9           |
| Jhon       | vehiculo.py, bicicleta.py, volador.py, avion.py, pajaro.py, coche.py, excepcionPersonalizada.py  | 4, 5, 6, 8, 10    |
| Todos      | main.py                                                                                          |                   |

## 👥 Equipo de Trabajo
* **Johan Marcelo Rojas** - *Ingeniería de Sistemas*
* **Jhon Jairo Linares** - *Ingeniería de Sistemas*
* **Isabella Betancur** - *Ingeniería de Sistemas*

---

## 🛠️ Guía de Configuración desde Cero (Windows)

Para poder ejecutar o modificar este código, necesitas preparar tu computadora. Sigue estos pasos en orden:

### 1. Instalación de Herramientas Básicas
Descarga e instala las siguientes tres herramientas (usa las opciones por defecto en los instaladores):

1.  **Python 3.x:** [Descargar aquí](https://www.python.org/downloads/). 
    * **⚠️ CRÍTICO:** Al instalar, marca la casilla que dice **"Add Python to PATH"**. Si no lo haces, nada funcionará.
2.  **Git:** [Descargar aquí](https://git-scm.com/download/win). Esto permite descargar y gestionar el código.
3.  **Visual Studio Code (VS Code):** [Descargar aquí](https://code.visualstudio.com/). Es el editor donde verás y editarás el código.

### 2. Descargar el Repositorio
Existen dos formas de bajar el trabajo a tu PC:

* **Opción A (Profesional):** Abre una terminal (CMD o PowerShell) y escribe:
    ```bash
    git clone [https://github.com/OverlordUrukEx/Programacion-1_taller_practico.git](https://github.com/OverlordUrukEx/Programacion-1_taller_practico.git)
    ```
* **Opción B (Rápida):** Haz clic en el botón verde **"Code"** en esta página y selecciona **"Download ZIP"**. Extrae la carpeta en tu escritorio.

### 3. Configuración del Editor (VS Code)
1. Abre **Visual Studio Code**.
2. Ve al menú `Archivo` > `Abrir Carpeta` y selecciona la carpeta que descargaste.
3. En la barra lateral izquierda, haz clic en el icono de **Extensiones** (cuadros pequeños) y busca **"Python"** (de Microsoft). Dale a **Instalar**.

### 4. Ejecución del Trabajo
1. Dentro de VS Code, abre uno de los archivos `.py` (ej. `main.py`).
2. Presiona la tecla `F5` o haz clic en el botón de **Play** (triángulo) en la esquina superior derecha.
3. Los resultados aparecerán en la parte inferior, en la pestaña llamada **Terminal**.

---

## 📂 Estructura del Proyecto
PROGRAMACION-1_TALLER_PRACTICO/
│
├── recursos/
│   ├── excepciones/
│   │   └── excepcionPersonalizada.py
│   │
│   └── modelos/
│       ├── animales/
│       │   ├── animal.py
│       │   ├── gato.py
│       │   ├── pajaro.py
│       │   ├── pato.py
│       │   ├── perro.py
│       │   └── vaca.py
│       │
│       ├── interfaces/
│       │   └── volador.py
│       │
│       └── transporte/
│           ├── avion.py
│           ├── bicicleta.py
│           ├── carro.py
│           ├── coche.py
│           ├── motor.py
│           └── vehiculo.py
│
├── main.py
├── .gitignore
└── README.md

## 📝 Notas de Desarrollo
* El código sigue los estándares de la asignatura de **Programación I**.
* Se utiliza **Programación Orientada a Objetos (POO)**.
* Se cumplen los requisitos del documento facilitado.

---
*Facultad de Ingeniería - Universidad de Manizales*