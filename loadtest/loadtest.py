"""Навантажувальний тест molotov: сервер має повертати JSON з кодом 200."""
from molotov import scenario

URL = "http://127.0.0.1:8080/"


@scenario(weight=100)
async def get_json(session):
    async with session.get(URL) as resp:
        assert resp.status == 200
        assert resp.headers["Content-Type"].startswith("application/json")
        data = await resp.json()
        assert data["status"] == "ok"
