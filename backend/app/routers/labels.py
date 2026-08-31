import io
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import qrcode
from .. import crud
from ..database import get_db

router = APIRouter(prefix="/items", tags=["labels"])

@router.get("/{item_id}/label")
def get_label(item_id: str, db: Session = Depends(get_db)):
    if not crud.get_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    img = qrcode.make(item_id)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
