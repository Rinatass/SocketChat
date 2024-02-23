from fastapi import APIRouter
from starlette.websockets import WebSocket

router = APIRouter()

connections = []


@router.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str) -> None:
    await websocket.accept()
    connections.append(websocket)
    while True:
        message = await websocket.receive_text()
        for connection in connections:
            await connection.send_text(f"{username}:{message}")
