from commands import fun
from services.api import post_burger_count

COMMANDS = {
    "!ping": fun.ping,
}

async def handle_message(message):
    handler = COMMANDS.get(message.content)
    if handler:
        await handler(message)

    count = message.content.lower().count("burger")
    if count > 0:
        await post_burger_count(str(message.author), count)
