from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Recipe(Base):
    __tablename__ = "recipe"

    recipe_id = Column(Integer, primary_key=True, index=True)
    recipe_name = Column(String, unique=True)



