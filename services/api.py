import os
import aiohttp

API_URL = os.environ["BURGER_API_URL"]
API_KEY = os.environ["BURGER_API_KEY"]

async def post_burger_count(user: str, count: int):
    async with aiohttp.ClientSession() as session:
        await session.post(
            f"{API_URL}/burger",
            headers={"x-api-key": API_KEY},
            json={"username": user, "count": count},
        )
