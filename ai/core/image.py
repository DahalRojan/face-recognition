import numpy as np
import cv2
from fastapi.exceptions import HTTPException
from ai.core.settings import HOST, IMAGE_DIR
from ai.core.utils import get_filename

class Image:
    def __init__(self, image=None, path=None):
        if isinstance(image, np.ndarray):
            self.image = image
        elif path:
            self.image = cv2.imread(str(path))
            if not isinstance(self.image, np.ndarray):
                raise HTTPException(
                    status_code=400,
                    detail='Given file either corrupted or not a image file'
                )
        else:
            raise ValueError('you must load an image')
            
    def grey(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def image2url(image):
        filepath = get_filename(IMAGE_DIR, file_name="image.png")
        filename = str(filepath).split('/')[-1]
        cv2.imwrite(str(filepath), image)
        url =f'{HOST}/images/{filename}'
        return url
            