from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)       # e.g. MSP-00001
    track = Column(String, nullable=False)                  # "new" | "used"
    category = Column(String, nullable=False)
    brand = Column(String, default="")
    part_name = Column(String, nullable=False)
    models = Column(String, default="")                     # compatible vehicle models
    condition = Column(String, default="")
    serial = Column(String, default="")                     # manufacturer barcode/serial, blank for used
    quantity = Column(Integer, default=0)
    bin_location = Column(String, default="")
    cost_price = Column(Float, default=0)
    sell_price = Column(Float, default=0)
    notes = Column(String, default="")
    has_photo = Column(Boolean, default=False)
    date_added = Column(DateTime(timezone=True), server_default=func.now())
