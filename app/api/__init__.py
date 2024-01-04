from fastapi import APIRouter
from app.api.endpoints import configuracao_cliente, aprovadores_cliente, tipos_rating_cliente, alcadas_cliente

api_router = APIRouter()

api_router.include_router(
    configuracao_cliente.router,
    prefix="/configuracao-cliente",
    tags=["configuracao_cliente"],
)

api_router.include_router(
    aprovadores_cliente.router,
    prefix="/aprovadores-cliente",
    tags=["aprovadores_cliente"],
)

api_router.include_router(
    tipos_rating_cliente.router,
    prefix="/tipos_rating-cliente",
    tags=["tipos_rating_cliente"],
)

api_router.include_router(
    alcadas_cliente.router,
    prefix="/alcadas-cliente",
    tags=["alcadas_cliente"],
)


