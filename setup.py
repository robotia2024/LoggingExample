from setuptools import setup, find_packages

# Leemos el archivo README para usarlo como la descripción larga del proyecto
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # 1. Datos básicos del paquete
    name="mi-super-app",             # El nombre con el que se instalará (ej: pip install mi-super-api)
    version="1.0.0",                 # La versión de tu software
    author="Tu Nombre o Empresa",
    author_email="tu-email@ejemplo.com",
    description="Una API increíble desarrollada con Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",

    # 2. ¿Dónde está el código de Python?
    # find_packages() busca automáticamente las carpetas que tengan un archivo __init__.py (como 'mi_api')
    packages=find_packages(),

    # 3. Restricciones del sistema
    python_requires=">=3.9",         # Tu APP solo funcionará en Python 3.9 o superior

    # 4. LAS DEPENDENCIAS (¡Súper importante!)
    # Esto reemplaza o complementa al archivo requirements.txt.
    # Cuando alguien instale tu paquete, pip instalará estas librerías automáticamente.
    install_requires=[
        # "fastapi>=0.100.0",
        # "uvicorn>=0.22.0",
        # "pydantic>=2.0.0",
        # "requests>=2.31.0",
    ],

    # 5. Clasificadores (Opcional, ayuda a identificar tu proyecto en internet)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
            "console_scripts": [
                "mi-app=app.main:main",
            ]
        },
)