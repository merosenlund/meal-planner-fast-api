from enum import Enum
from typing import Union

from pydantic import BaseModel


class RecipeIn(BaseModel):
    recipe_name: str
    is_active: bool = True


class RecipeOut(BaseModel):
    recipe_id: int
    recipe_name: str
    is_active: bool


class RecipeUpdate(BaseModel):
    recipe_name: str | None
    is_active: bool | None
