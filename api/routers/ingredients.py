from fastapi import APIRouter, HTTPException

from models.ingredients import (
    IngredientIn, IngredientOut, IngredientUpdate
)
from db_interface.ingredients import (
    get_ingredient,
    get_all_ingredients,
    add_ingredient,
    update_ingredient
)


router = APIRouter(
    prefix='/ingredients',
    tags=["Ingredients"],
    responses={404: {"message": "Not found"}},
)


@router.get("/{ingredient_id}", response_model=IngredientOut)
def api_get_ingredient(ingredient_id: int):
    ingredient = get_ingredient(ingredient_id)
    if ingredient == None:
        raise HTTPException(status_code=404, detail="Item not found")
    return ingredient


@router.get("/", response_model=list[IngredientOut])
def api_get_ingredients(page: int = 1, count: int = 10, ):
    ingredients = get_all_ingredients(page=page, count=count)
    return ingredients


@router.post("/", response_model=IngredientOut)
def api_create_ingredient(ingredient: IngredientIn):
    ingredient_values = add_ingredient(ingredient)
    return ingredient_values


@router.put("/{ingredient_id}")
def api_update_ingredient(ingredient_id: int, data: IngredientUpdate):
    ingredient = update_ingredient(ingredient_id, data.dict(exclude_unset=True))
    return ingredient