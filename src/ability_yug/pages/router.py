from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix = '',
    tags=["frontend"]
)

templates = Jinja2Templates(directory='src/ability_yug/templates')

@router.get('/main')
async def get_main_page(request: Request):
    return templates.TemplateResponse(name="main.html", context={'request': request})