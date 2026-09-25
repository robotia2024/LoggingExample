#!/bin/bash

# 0. Detener el script inmediatamente si ocurre algún error
set -e

# 1. Capturar la versión de fecha_hora enviada por GitHub
VERSION=$1
APP_NAME="mi_app"
WHEEL_FILE="/home/ubuntu/builds/dist/${APP_NAME}-${VERSION}-py3-none-any.whl"
DEPLOY_DIR="/home/ubuntu/mi-app"

echo "🚀 Iniciando Dev Deploy para la versión basada en tiempo: $VERSION..."

# 2. Validar que el archivo wheel con esa marca de tiempo exista
if [ ! -f "$WHEEL_FILE" ]; then
    echo "❌ Error: No se encontró el build esperado en $WHEEL_FILE"
    exit 1
fi

# 3. Entrar al directorio y validar el entorno virtual (Venv)
mkdir -p $DEPLOY_DIR
cd $DEPLOY_DIR || exit

if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual de Python..."
    python3 -m venv venv
fi

# 4. Activar el entorno e instalar la versión específica
echo "⚡ Instalando el paquete Wheel..."
source venv/bin/activate
pip install --upgrade pip
pip install "$WHEEL_FILE" --force-reinstall

# 5. Reiniciar el microservicio en segundo plano
echo "🔄 Reiniciando el proceso de la API..."
pkill -f "uvicorn $APP_NAME" || true

# Guardamos un registro interno de cuál fue la última versión desplegada con éxito
echo "$VERSION" > la_ultima_version_dev_deploy_ok.txt

nohup uvicorn ${APP_NAME}.main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &

echo "✅ Despliegue de la versión $VERSION finalizado correctamente."