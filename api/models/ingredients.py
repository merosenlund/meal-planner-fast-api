from enum import Enum
from typing import Union

from pydantic import BaseModel


class IngredientType(str, Enum):
    standard = "STANDARD"
    fruit = "FRUIT"
    veggie = "VEGGIE"


class IngredientIn(BaseModel):
    name: str
    unit_of_measure: str
    type: IngredientType = "STANDARD"


class IngredientOut(BaseModel):
    ingredient_id: int
    ingredient_name: str
    unit_of_measure: str
    ingredient_type: str


class IngredientUpdate(BaseModel):
    ingredient_name: Union[str, None]
    unit_of_measure: Union[str, None]
    ingredient_type: Union[IngredientType, None]