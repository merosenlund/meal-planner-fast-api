from fastapi import FastAPI
from routers import recipes, ingredients

app = FastAPI()


app.include_router(recipes.router)
app.include_router(ingredients.router)