from services.api import get_burger_total, post_burger_count

async def ping(message):
    await message.channel.send("scam")

async def burgers(message):
    total = await post_burger_count(str(message.author), 1)
    await message.channel.send(f"There are: {int(total)} burgers")
