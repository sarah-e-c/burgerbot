import os
import aiohttp

API_URL = os.environ["BURGER_API_URL"]
API_KEY = os.environ["BURGER_API_KEY"]

async def get_burger_total() -> int:
    async with aiohttp.ClientSession() as session:
        resp = await session.get(f"{API_URL}/burger")
        data = await resp.json()
        return data["count"]

async def post_burger_count(user: str, count: int) -> int:
    async with aiohttp.ClientSession() as session:
        resp = await session.post(
            f"{API_URL}/burger",
            headers={"x-api-key": API_KEY},
            json={"username": user, "count": count},
        )
        data = await resp.json()
        return data["count"]
