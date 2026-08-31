from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def next_internal_id(db: Session) -> str:
    count = db.query(func.count(models.Item.id)).scalar() or 0
    # Loop guards against gaps left by deleted items colliding with a reused number
    candidate_n = count + 1
    while db.get(models.Item, f"MSP-{candidate_n:05d}"):
        candidate_n += 1
    return f"MSP-{candidate_n:05d}"

def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    db_item = models.Item(id=next_internal_id(db), **item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, track: str | None = None, search: str | None = None):
    query = db.query(models.Item)
    if track:
        query = query.filter(models.Item.track == track)
    if search:
        like = f"%{search}%"
        query = query.filter(
            (models.Item.part_name.ilike(like)) |
            (models.Item.brand.ilike(like)) |
            (models.Item.models.ilike(like)) |
            (models.Item.id.ilike(like))
        )
    return query.order_by(models.Item.date_added.desc()).all()

def get_item(db: Session, item_id: str):
    return db.get(models.Item, item_id)

def update_item(db: Session, item_id: str, updates: schemas.ItemUpdate):
    db_item = db.get(models.Item, item_id)
    if not db_item:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: str) -> bool:
    db_item = db.get(models.Item, item_id)
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True

def mark_has_photo(db: Session, item_id: str, value: bool):
    db_item = db.get(models.Item, item_id)
    if db_item:
        db_item.has_photo = value
        db.commit()
