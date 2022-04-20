from typing import Optional

from sqlmodel import Field, SQLModel


class HairProductBase(SQLModel):
    product_name: str
    product_brand: str
    product_type: str
    straight: Optional[bool]
    wavy: Optional[bool]
    curly: Optional[bool]
    coily: Optional[bool]
    fine: Optional[bool]
    medium: Optional[bool]
    thick: Optional[bool]
    image_link: Optional[str]


class HairProduct(HairProductBase, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)


class HairProductCreate(HairProductBase):
    pass


class HairProductRead(HairProductBase):
    product_id: int


class HairProductUpdate(SQLModel):
    product_name: Optional[str] = None
    product_category: Optional[str] = None
    product_type: Optional[str] = None
    straight: Optional[bool] = None
    wavy: Optional[bool] = None
    curly: Optional[bool] = None
    coily: Optional[bool] = None
    fine: Optional[bool] = None
    medium: Optional[bool] = None
    thick: Optional[bool] = None
