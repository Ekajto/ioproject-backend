from typing import List, Optional

from fastapi import Depends, Query
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlmodel import Session, col, or_, select

from app.core import auth, db
from app.models.SkinProduct import SkinProduct, SkinProductCreate, SkinProductUpdate
from app.models.Token import Token

router = SQLAlchemyCRUDRouter(
    schema=SkinProduct,
    create_schema=SkinProductCreate,
    update_schema=SkinProductUpdate,
    db_model=SkinProduct,
    db=db.get_session,
    dependencies=[Depends(auth.validate_token)],
    prefix="SkinProduct",
)


@router.get("")
def get_all_skin_product(
    *,
    session: Session = Depends(db.get_session),
    token: Token = Depends(auth.validate_token),
    ids: Optional[List[int]] = Query(default=None),
    query: Optional[str] = Query(default=None),
    oily: Optional[bool] = Query(default=None),
    dry: Optional[bool] = Query(default=None),
    normal: Optional[bool] = Query(default=None),
    page: Optional[int] = Query(default=1),
    size: Optional[int] = Query(default=50),
):
    offset = (page - 1) * size
    limit = size
    db_query = select(SkinProduct).offset(offset).limit(limit)
    query_params = {"ids": ids, "query": query, "oily": oily, "dry": dry, "normal": normal}

    query_params = {key: value for key, value in query_params.items() if value is not None}

    for key, value in query_params.items():
        if key == "ids":
            db_query = db_query.where(SkinProduct.product_id.in_(value))
        elif key == "query":
            db_query = db_query.where(
                or_(col(SkinProduct.product_brand).contains(value), col(SkinProduct.product_name).contains(value))
            )
        else:
            db_query = db_query.where(getattr(SkinProduct, key) == value)

    results = session.exec(db_query).all()
    return results
