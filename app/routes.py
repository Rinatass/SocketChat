from fastapi import APIRouter, websockets
from jinja2 import Environment, FileSystemLoader
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket

router = APIRouter()
env = Environment(loader=FileSystemLoader('app/templates'))


@router.get("/", response_class=HTMLResponse)
async def main():
    template = env.get_template('chat.html')
    return template.render()