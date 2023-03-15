import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__name__).resolve().parent
TEMP_DIR = BASE_DIR / 'temp'
ASSETS_DIR = BASE_DIR / 'assets'
IMAGE_DIR = ASSETS_DIR / 'images'

HOST = os.environ['HOST']