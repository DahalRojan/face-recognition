from pydantic import BaseModel
from typing import Optional

class FaceRecognitionResponse(BaseModel):
    is_similar: bool
    similarity : float
    match_index: int
    nfaces: int
    image1: str
    image1_landmark:str | None = None
    image2: str
    image2_landmark:str | None = None



