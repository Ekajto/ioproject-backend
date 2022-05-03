from typing import List, Optional

from fastapi import Depends, Query
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlmodel import Session, or_, select

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
):
    if not ids and not query:
        query = select(SkinProduct)
    elif ids and not query:
        query = select(SkinProduct).where(SkinProduct.product_id.in_(ids))
    elif not ids and query:
        query = select(SkinProduct).where(or_(SkinProduct.product_brand == query, SkinProduct.product_name == query))
    else:
        query = (
            select(SkinProduct)
            .where(SkinProduct.product_id.in_(ids))
            .where(or_(SkinProduct.product_brand == query, SkinProduct.product_name == query))
        )
    results = session.exec(query).all()
    return results
