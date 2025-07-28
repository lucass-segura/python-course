# Entornos Virtuales en Python

---
## 1. Creación de un Entorno Virtual
Para crear un nuevo entorno virtual, utilizamos el siguiente comando en la terminal. Esto creará una carpeta (en este caso, llamada `env`) que contendrá una instalación de Python y sus paquetes de forma aislada.

```bash
python -m venv env
```

-   `python`: Invoca al intérprete de Python.
-   `-m venv`: Le indica a Python que ejecute el módulo `venv`.
-   `env`: Es el nombre que le damos al entorno virtual.

---
## 2. Activación del Entorno Virtual
Una vez creado, es necesario activar el entorno para empezar a utilizarlo. El comando varía según el sistema operativo.

### Windows (cmd, PowerShell o Git Bash)
```bash
# cmd o PowerShell
.env\Scripts\activate
```

### Linux o macOS
```bash
source .env/bin/activate
```

> **Nota:** Al activar el entorno, notarás que el nombre del mismo (`(env)` en este caso) aparecerá al inicio de la línea de tu terminal, indicando que está activo.

---
## 3. Desactivación del Entorno Virtual
Cuando se termina de trabajar en el proyecto, se puede desactivar el entorno con un simple comando.

```bash
deactivate
```

---
## 4. Gestión de Dependencias con PIP
Los entornos virtuales permiten manejar las dependencias de cada proyecto de forma separada.

### Listar Paquetes Instalados
Para ver todos los paquetes que has instalado en el entorno virtual activo se usa `pip freeze`.

```bash
pip freeze
```

### Exportar Dependencias a un Archivo
Es una buena práctica guardar la lista de dependencias en un archivo `requirements.txt`.

```bash
pip freeze > requirements.txt
```

### Instalar Dependencias desde un Archivo
Si clonas un proyecto que contiene un archivo `requirements.txt`, se pueden instalar todas las dependencias necesarias con un solo comando.

```bash
pip install -r requirements.txt
```
