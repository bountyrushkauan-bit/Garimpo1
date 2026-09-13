from datetime import datetime

from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    category: str
    store: str
    url: str
    price: float
    old_price: float | None = None
    is_deal: bool = False

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    checked_at: datetime
    model_config = ConfigDict(from_attributes=True)
