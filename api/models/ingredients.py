from typing import Union

from pydantic import BaseModel


class IngredientIn(BaseModel):
    name: int
    unit_of_measure: float
    type: str = "STANDARD"


class IngredientOut(BaseModel):
    id: int
    name: str
    unit_of_measure: float
    type: str


class IngredientList(BaseModel):
    ingredients: list[IngredientOut]