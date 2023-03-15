import urllib3
import shutil
from fastapi import UploadFile
from fastapi.exceptions import HTTPException
from ai.core.settings import TEMP_DIR
from ai.core.utils import get_filename


class File:
    @staticmethod
    def handle_download(url : str):
        filename = get_filename(TEMP_DIR, 'image.png')
        pool = urllib3.PoolManager()
        pool.addheaders = [(
            'User-Agent',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'
        )]
        try:
            with open(filename, 'wb') as buffer:
                response = pool.request('GET', url, preload_content=False)
                shutil.copyfileobj(response, buffer)
        except Exception as exp:
            raise HTTPException(status_code=424, detail="Couldn't download the image")
        
        return filename
    
    @staticmethod
    def handle_upload(upload_file: UploadFile):
        filename = get_filename(TEMP_DIR, 'image.png')
        with open(filename, 'wb') as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        return filename
