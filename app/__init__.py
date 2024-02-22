from fastapi import FastAPI
from app.routes import router
from app.websockets import router as websocket_router
app = FastAPI()
app.include_router(router)
app.include_router(websocket_router)
