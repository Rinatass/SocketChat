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
    ws_host = os.environ.get('WS_HOST')
    template = env.get_template('chat.html')
    return template.render(username=username, ws_host=ws_host)


@router.get("/about", response_class=HTMLResponse)
async def about():
    template = env.get_template('about.html')
    return template.render()


@router.get("/author", response_class=HTMLResponse)
async def author():
    template = env.get_template('author.html')
    return template.render()
