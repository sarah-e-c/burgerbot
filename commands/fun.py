from services.api import get_burger_total

async def ping(message):
    await message.channel.send("scam")

async def burgers(message):
    total = await get_burger_total()
    await message.channel.send(f"Total burgers: {total}")
