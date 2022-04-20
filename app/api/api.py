from fastapi import APIRouter

from app.api.endpoints import hair_product, login, skin_product

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(hair_product.router)
api_router.include_router(skin_product.router)
