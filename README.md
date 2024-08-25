# Space Invader

¡Bienvenido al proyecto **Space Invader**! Este es un juego clásico de invasores espaciales desarrollado con Pygame y gestionado mediante un servidor ASGI con Uvicorn.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- `pip` para la gestión de paquetes

## Instalación

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/tu_usuario/space_invader.git
cd space_invader
```

### 2. Crear el Entorno Virtual

Crea un entorno virtual para aislar las dependencias del proyecto. Usa el siguiente comando:

```bash
python -m venv package
```

### 3. Activar el Entorno Virtual

- En Windows:

```bash
package\Scripts\activate
```

- En macOS/Linux:

```bash
source package/bin/activate
```

### 4. Instalar las Dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el Servidor con Uvicorn

Para iniciar el servidor con Uvicorn y ejecutar el archivo main.py, utiliza el siguiente comando:

```bash
uvicorn main:app
```

### Estructura del proyecto

```bash
Space_invader/
│
├── icons/                  # Imágenes y recursos del juego
├── music/                  # (chihiro - billie eilish)
├── sounds/                 # Sonidos complementarios del juego
├── package/                # Entorno virtual y paquetes
├── main.py                 # Archivo principal del juego
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Instrucciones del proyecto
```

### ¡Gracias por jugar a Space Invader! 🚀👾

Creado por Carlos Andres Alzate Mejia
