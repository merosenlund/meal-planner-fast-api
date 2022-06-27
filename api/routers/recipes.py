from fastapi import APIRouter

router = APIRouter(
    prefix='/recipes',
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"this": "is fake"}

@router.get("/")
async def read_items():
    return fake_items_db