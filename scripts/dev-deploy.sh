#!/bin/bash

# 🛑 1. Detener el script inmediatamente si ocurre algún error
set -e

# 📁 2. Definir rutas (Configura esto según tu servidor)
APP_DIR="/var/www/mi-api"
VENV_DIR="$APP_DIR/venv"

echo "🚀 Iniciando el despliegue de la API... establecer variables entorno, echo messsages de sus valores"

# STOP SERVICE
# SET UNDER MAINTENANCE MESSAGE IN THE SERVICE

# 📂 3. Moverse a la carpeta del proyecto
cd $APP_DIR

# 📥 4. Descargar los últimos cambios desde GitHub
echo "📥 Descargando la última versión desde producción..."
git fetch origin main
git reset --hard origin/main

# 🐍 5. Activar el entorno virtual de Python e instalar dependencias
echo "📦 Actualizando dependencias de Python..."
source $VENV_DIR/bin/activate
pip install --upgrade pip
pip install .  # O 'pip install -r requirements.txt' si no usas setup.py

# 🗄️ 6. Ejecutar migraciones de Base de Datos (Muy típico en Django o FastAPI con Alembic)
echo "🗄️ Ejecutando migraciones de la base de datos... i.e. changelogs"
# python -m alembic upgrade head  # (Descomenta si usas Alembic)
# python manage.py migrate        # (Descomenta si usas Django)

# 🔄 7. Reiniciar EL SERVICIO/la API para que cargue el código nuevo
echo "🔄 Reiniciando el servicio de la API..."
# 'mi-api' es el servicio que creaste en el servidor para correr Gunicorn o Uvicorn
sudo systemctl restart mi-app

echo "✅ ¡Despliegue finalizado con éxito!"