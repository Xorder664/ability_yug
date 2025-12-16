from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.ability_yug.pages.router import router as router_pages

app = FastAPI()

app.mount('/static', StaticFiles(directory='src/ability_yug/static'), 'static')
templates = Jinja2Templates(directory='src/ability_yug/templates')

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return {"path": full_path}