🚀 Enterprise Microservices Stack: Python, Docker & Keycloak
Este proyecto es una arquitectura de microservicios de alto rendimiento diseñada bajo el patrón API Gateway y Database-per-Service, optimizada para entornos con 32GB de RAM y seguridad centralizada.

🏗️ Arquitectura Técnica
API Gateway (Nginx): Punto de entrada único (Puerto 80) con reglas de rewrite para limpieza de rutas y proxy_cache en memoria.

IAM (Keycloak): Gestión de identidad y acceso en /auth/.

Microservicios (FastAPI): user-service y product-service aislados.

Caché de Seguridad (Redis): Implementación de Token Introspection Caching para reducir la latencia en la validación de JWT.

Persistencia (PostgreSQL): Bases de datos independientes (db_users y db_products) para garantizar el desacoplamiento total.

📂 Estructura del Proyecto
/proyecto_empresarial
├── docker-compose.yaml      # Orquestador maestro
├── gateway/
│   └── nginx.conf           # Configuración de Proxy Inverso y Caché
├── user-service/            # Microservicio de Usuarios (Port 8001)
│   ├── auth.py              # Lógica de validación JWT + Redis
│   ├── database.py          # SQLAlchemy + PostgreSQL
│   └── main.py              # FastAPI Endpoints
├── product-service/         # Microservicio de Productos (Port 8002)
│   ├── ...
├── frontend/
│   └── index.html           # Dashboard de prueba
└── .env                     # Variables de entorno (No subir a Git)

🛠️ Requisitos Previos
Docker y Docker Compose

RAM mínima recomendada: 8GB (Optimizado para 32GB)

Python 3.11+ (para desarrollo local)

🚀 Despliegue Rápido
Clonar el repositorio:

git clone https://github.com/tu-usuario/proyecto-microservicios.git
cd proyecto-microservicios

Levantar la infraestructura:

docker-compose up -d --build

Verificar contenedores:

docker ps

🔌 Endpoints Principales
Servicio                  Ruta Externa           Puerto Interno
Frontend                  UI                     http://localhost/80        
Keycloak                  IAM                    http://localhost/auth/8080
User                      Service                http://localhost/api/users/8001
Product                   Service                http://localhost/api/products/8002

⚡ Optimizaciones de Rendimiento
Nginx Cache: Se utiliza una keys_zone de 10MB para almacenar metadatos de respuesta, reduciendo la carga en los servicios de Python.

Keepalive: Configurado a 65s para minimizar el overhead de apretón de manos TCP en conexiones recurrentes.

Redis LRU: El contenedor de caché utiliza una política allkeys-lru con un límite de 2GB para asegurar que la validación de tokens sea instantánea.

🔒 Seguridad
El acceso a los microservicios requiere un token JWT emitido por Keycloak.

El cliente solicita el token a /auth/.

El Gateway redirige la petición al microservicio correspondiente.

El microservicio verifica el token contra Redis. Si no existe o expiró, realiza introspección en Keycloak.

📄 Licencia
Este proyecto está bajo la Licencia MIT.
