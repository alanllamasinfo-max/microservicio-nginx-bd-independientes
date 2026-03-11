#!/bin/bash

echo "🚀 Iniciando configuración del Proyecto Empresarial..."

# 1. Crear directorios para volúmenes si no existen
echo "📁 Creando directorios de persistencia..."
mkdir -p pg_users_data pg_products_data redis_data nginx_cache

# 2. Asegurar permisos (especialmente para contenedores que corren como non-root)
chmod -R 777 pg_users_data pg_products_data redis_data nginx_cache

# 3. Limpiar contenedores antiguos (opcional, para evitar conflictos)
echo "🧹 Limpiando despliegues anteriores..."
docker-compose down --remove-orphans

# 4. Construir y levantar
echo "🏗️ Construyendo imágenes y levantando servicios..."
docker-compose up -d --build

echo "✅ ¡Todo listo!"
echo "-------------------------------------------------------"
echo "🌐 Frontend: http://localhost"
echo "🔐 Keycloak: http://localhost/auth/ (Realm: enterprise-realm)"
echo "👥 User Service: http://localhost/api/users/"
echo "📦 Product Service: http://localhost/api/products/"
echo "-------------------------------------------------------"
echo "💡 Tip: Usa 'docker-compose logs -f' para ver la salida en tiempo real."
