from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItemCreate(BaseModel):
    track: str                 # "new" | "used"
    category: str
    brand: Optional[str] = ""
    part_name: str
    models: Optional[str] = ""
    condition: Optional[str] = ""
    serial: Optional[str] = ""
    quantity: int = 0
    bin_location: Optional[str] = ""
    cost_price: float = 0
    sell_price: float = 0
    notes: Optional[str] = ""

class ItemUpdate(BaseModel):
    category: Optional[str] = None
    brand: Optional[str] = None
    part_name: Optional[str] = None
    models: Optional[str] = None
    condition: Optional[str] = None
    serial: Optional[str] = None
    quantity: Optional[int] = None
    bin_location: Optional[str] = None
    cost_price: Optional[float] = None
    sell_price: Optional[float] = None
    notes: Optional[str] = None

class ItemOut(ItemCreate):
    id: str
    has_photo: bool
    date_added: datetime

    class Config:
        from_attributes = True
