from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.core import auth
from app.core.db import get_session
from app.models.HairProduct import HairProduct, HairProductCreate, HairProductUpdate

router = SQLAlchemyCRUDRouter(
    schema=HairProduct,
    create_schema=HairProductCreate,
    update_schema=HairProductUpdate,
    db_model=HairProduct,
    db=get_session,
    dependencies=[Depends(auth.validate_token)],
    prefix="hairProduct",
)
