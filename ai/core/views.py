import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from ai.core.settings import IMAGE_DIR

router = APIRouter()

@router.get("/images/{fpath:path}", tags=["default"])
def image_download(fpath: str):
    if not os.path.exists(IMAGE_DIR / fpath):
        raise HTTPException(status_code=404, detail='file not found')
    return FileResponse(IMAGE_DIR / fpath)
