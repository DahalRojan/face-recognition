from fastapi import FastAPI
from ai.recognition.views import router as recognition_router
from ai.core.views import router as default_router

def init_routers(app: FastAPI):
    app.include_router(default_router)
    app.include_router(recognition_router)