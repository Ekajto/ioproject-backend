from typing import List, Optional

from fastapi import Depends, Query
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlmodel import Session, col, or_, select

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
    straight: Optional[bool] = Query(default=None),
    wavy: Optional[bool] = Query(default=None),
    curly: Optional[bool] = Query(default=None),
    coily: Optional[bool] = Query(default=None),
    fine: Optional[bool] = Query(default=None),
    medium: Optional[bool] = Query(default=None),
    thick: Optional[bool] = Query(default=None),
    page: Optional[int] = Query(default=1),
    size: Optional[int] = Query(default=50),
):
    offset = (page - 1) * size
    limit = size
    db_query = select(HairProduct).offset(offset).limit(limit)
    query_params = {
        "ids": ids,
        "query": query,
        "straight": straight,
        "wavy": wavy,
        "curly": curly,
        "coily": coily,
        "fine": fine,
        "medium": medium,
        "thick": thick,
    }

    query_params = {key: value for key, value in query_params.items() if value is not None}

    for key, value in query_params.items():
        if key == "ids":
            db_query = db_query.where(HairProduct.product_id.in_(value))
        elif key == "query":
            db_query = db_query.where(
                or_(col(HairProduct.product_brand).contains(value), col(HairProduct.product_name).contains(value))
            )
        else:
            db_query = db_query.where(getattr(HairProduct, key) == value)

    results = session.exec(db_query).all()
    return results
