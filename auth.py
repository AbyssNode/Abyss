# auth.py

from fastapi import Request, HTTPException
from fastapi.security.api_key import APIKeyHeader

# Define the API key header name
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Replace this with a secure method later (e.g. from environment variables)
VALID_API_KEYS = {"supersecretkey123"}

async def verify_api_key(request: Request, api_key: str = None):
    if api_key is None:
        api_key = request.headers.get(API_KEY_NAME)

    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
