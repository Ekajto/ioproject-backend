from typing import List, Optional

from fastapi import Depends, Query
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlmodel import Session, or_, select

from app.core import auth, db
from app.models.HairProduct import HairProduct, HairProductCreate, HairProductUpdate
from app.models.Token import Token

router = SQLAlchemyCRUDRouter(
    schema=HairProduct,
    create_schema=HairProductCreate,
    update_schema=HairProductUpdate,
    db_model=HairProduct,
    db=db.get_session,
    dependencies=[Depends(auth.validate_token)],
    prefix="hairProduct",
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
        query = select(HairProduct)
    elif ids and not query:
        query = select(HairProduct).where(HairProduct.product_id.in_(ids))
    elif not ids and query:
        query = select(HairProduct).where(or_(HairProduct.product_brand == query, HairProduct.product_name == query))
    else:
        query = (
            select(HairProduct)
            .where(HairProduct.product_id.in_(ids))
            .where(or_(HairProduct.product_brand == query, HairProduct.product_name == query))
        )
    results = session.exec(query).all()
    return results
