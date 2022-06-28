from fastapi import APIRouter

router = APIRouter(
    prefix='/recipes',
    tags=["Recipes"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"this": "is fake"}

@router.get("/")
async def get_recipes():
    return fake_items_db