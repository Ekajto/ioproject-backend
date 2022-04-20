from fastapi import Depends, FastAPI

from app.api.api import api_router
from app.core import auth

app = FastAPI()


app.include_router(api_router)


@app.get("/")
async def read_root(token=Depends(auth.validate_token)):
    return {"Hello": "World"}
