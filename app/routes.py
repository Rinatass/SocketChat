from fastapi import APIRouter, Form
from jinja2 import Environment, FileSystemLoader
from starlette.responses import HTMLResponse
import os

router = APIRouter()
env = Environment(loader=FileSystemLoader('app/templates'))


@router.get("/", response_class=HTMLResponse)
async def main():
    template = env.get_template('login-form.html')
    return template.render()


@router.get("/chat", response_class=HTMLResponse)
async def chat(username):
    host = os.environ.get('host')
    template = env.get_template('chat.html')
    return template.render(username=username, host=host)
