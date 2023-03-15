from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai.core import init_routers

description = """
    A RESTful face recognition tool part of BitsKraft AI suit
"""

app = FastAPI(
    title="Bitskraft Face Recognition Api",
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