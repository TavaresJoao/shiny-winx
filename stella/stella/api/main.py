import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi

from .routers import endpoints

load_dotenv()

api = FastAPI()
api.include_router(endpoints.router)

def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema
    openapi_schema = get_openapi(
        title="Stella - API",
        version="1.0_beta",
        description="Serviço para Gerenciamento da Bdocker-compase de Exames",
        routes=api.routes
    )
    api.openapi_schema = openapi_schema
    return api.openapi_schema

api.openapi = custom_openapi

@api.get("/api/")
async def root():
    return {"message": "Welcome to Stella API"}