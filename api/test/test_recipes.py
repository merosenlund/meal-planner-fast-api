from fastapi.testclient import TestClient

from ..routers.recipes import router

client = TestClient(router)


def test_get_recipes_returns_200_code():
    response = client.get("/recipes")
    assert response.status_code == 200