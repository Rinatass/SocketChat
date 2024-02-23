from fastapi import APIRouter, HTTPException
from starlette.websockets import WebSocket, WebSocketDisconnect

router = APIRouter()

connections = []


@router.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str) -> None:
    if username is None:
        return None
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            for connection in connections:
                await connection.send_text(f"{username}: {message}")
    except WebSocketDisconnect:
        connections.remove(websocket)
        for connection in connections:
            await connection.send_text(f"{username} left the chat")
