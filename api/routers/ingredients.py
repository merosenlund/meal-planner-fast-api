from fastapi import APIRouter

from models.ingredients import IngredientIn
from db_interface.ingredients import (
    get_all_ingredients,
    add_ingredient,
)

router = APIRouter(
    prefix='/ingredients',
    tags=["Ingredients"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_ingredients():
    ingredients = get_all_ingredients()
    return ingredients


@router.post("/")
async def create_ingredient(ingredient: IngredientIn):
    ingredient = add_ingredient(ingredient)
    return ingredient