import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMP_DIR = BASE_DIR / 'temp'
ASSETS_DIR = BASE_DIR / 'assets'
IMAGE_DIR = ASSETS_DIR / 'images'

HOST = os.environ.get('HOST', 'http://localhost:8000')