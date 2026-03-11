import redis
import requests
import os
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

REDIS_URL = os.getenv("REDIS_URL", "redis://redis_cache:6379/0")
KEYCLOAK_URL = http://keycloak:8080/realms/enterprise-realm
#KEYCLOAK_URL = os.getenv("KEYCLOAK_URL") # Ej: http://keycloak:8080/realms/master/protocol/openid-connect/token/introspect
cache = redis.from_url(REDIS_URL)

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    
    # 1. Intentar obtener del caché de Redis
    cached_user = cache.get(f"token:{token}")
    if cached_user:
        return {"active": True, "user": cached_user.decode('utf-8')}

    # 2. Si no está en caché, Introspección con Keycloak
    try:
        # Nota: Ajustar Client ID y Secret según tu config de Keycloak
        response = requests.post(
            f"{KEYCLOAK_URL}/protocol/openid-connect/token/introspect",
            data={"token": token, "client_id": "my-api-client", "client_secret": "secret"},
            timeout=5
        )
        data = response.json()
        
        if not data.get("active"):
            raise HTTPException(status_code=401, detail="Token inválido")

        # 3. Guardar en caché por 300 segundos (5 min) para optimizar
        cache.setex(f"token:{token}", 300, data.get("preferred_username", "unknown"))
        return data
        
    except Exception:
        raise HTTPException(status_code=401, detail="Error de autenticación")
