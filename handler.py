from commands import fun
from services.api import post_burger_count

COMMANDS = {
    "!ping": fun.ping,
    "!burgers": fun.burgers,
}

async def handle_message(message):
    handler = COMMANDS.get(message.content)
    if handler:
        await handler(message)

    count = message.content.lower().count("burger")
    if count > 0:
        total = await post_burger_count(str(message.author), count)
        await message.channel.send(f"Total burgers: {total}")
