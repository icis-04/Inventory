import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from .. import crud
from ..database import get_db
from ..config import settings

router = APIRouter(prefix="/items", tags=["photos"])

def _photo_path(item_id: str) -> str:
    return os.path.join(settings.PHOTO_DIR, f"{item_id}.jpg")

@router.post("/{item_id}/photo")
async def upload_photo(item_id: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not crud.get_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    contents = await file.read()
    with open(_photo_path(item_id), "wb") as f:
        f.write(contents)
    crud.mark_has_photo(db, item_id, True)
    return {"item_id": item_id, "saved": True}

@router.get("/{item_id}/photo")
def get_photo(item_id: str):
    path = _photo_path(item_id)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="No photo for this item")
    return FileResponse(path, media_type="image/jpeg")
