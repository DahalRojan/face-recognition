from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai.core import init_routers

description = """
    A RESTful face recognition tool
"""

app = FastAPI(
    title="Face Recognition API",
    description=description,
    version="2"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

init_routers(app)