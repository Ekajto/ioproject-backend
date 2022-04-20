from typing import Optional

from sqlmodel import Field, SQLModel


class SkinProductBase(SQLModel):
    product_name: str
    product_brand: str
    product_type: str
    oily: Optional[bool]
    dry: Optional[bool]
    normal: Optional[bool]
    image_link: Optional[str]


class SkinProduct(SkinProductBase, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)


class SkinProductCreate(SkinProductBase):
    pass


class SkinProductRead(SkinProductBase):
    product_id: int


class SkinProductUpdate(SQLModel):
    product_name: Optional[str] = None
    product_brand: Optional[str] = None
    product_type: Optional[str] = None
    oily: Optional[bool] = None
    dry: Optional[bool] = None
    normal: Optional[bool] = None
    image_link: Optional[str] = None
