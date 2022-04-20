from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.core import auth
from app.core.db import get_session
from app.models.SkinProduct import SkinProduct, SkinProductCreate, SkinProductUpdate

router = SQLAlchemyCRUDRouter(
    schema=SkinProduct,
    create_schema=SkinProductCreate,
    update_schema=SkinProductUpdate,
    db_model=SkinProduct,
    db=get_session,
    dependencies=[Depends(auth.validate_token)],
    prefix="SkinProduct",
)
