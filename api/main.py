from fastapi import FastAPI
from routers import recipes

app = FastAPI()


app.include_router(recipes.router)
