import os
from fastapi import APIRouter

router = APIRouter(
    prefix='/recipes',
    tags=["Recipes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def api_get_recipes():
    return os.getenv("PGHOST")