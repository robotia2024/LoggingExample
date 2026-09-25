#!/bin/bash
# eSTE SCRIPT ESTA EN EL SERVIDOR DE AWS QUE CORRE DOCKER
# Configurar variables
APP_NAME="mi-app"
PORT_SERVER=8000
PORT_CONTAINER=8000
PROJECT_DIR="/home/ubuntu/mi-app"  # Cambia esto por la ruta real en tu AWS

echo "🚀 Iniciando despliegue en AWS..."

# 1. Entrar a la carpeta y descargar + merge el último código de GitHub rama main
cd $PROJECT_DIR
git pull origin main

# 2. Detener y borrar la versión vieja
echo "🛑 Limpiando contenedor anterior..."
sudo docker stop $APP_NAME 2>/dev/null || true
sudo docker rm $APP_NAME 2>/dev/null || true

# 3. Construir la nueva imagen con el código actualizado
echo "📦 Construyendo nueva imagen de Docker..."
sudo docker build -t $APP_NAME:latest .

# 4. Encender la API
echo "⚡ Encendiendo contenedor..."
sudo docker run -d \
  --name $APP_NAME \
  -p $PORT_SERVER:$PORT_CONTAINER \
  --restart always \`
  $APP_NAME:latest

echo "✅ ¡$APP_NAME actualizada con éxito en AWS!"