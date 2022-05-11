from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.core import auth
from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
async def read_root(token=Depends(auth.validate_token)):
    return {"Hello": "World"}
