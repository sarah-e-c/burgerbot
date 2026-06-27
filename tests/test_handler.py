import pytest
from unittest.mock import AsyncMock, MagicMock, patch


def make_message(content, author="testuser"):
    message = MagicMock()
    message.content = content
    message.author = author
    message.channel.send = AsyncMock()
    return message


@pytest.mark.asyncio
async def test_ping_command():
    message = make_message("!ping")
    with patch("handler.post_burger_count", new=AsyncMock()) as mock_post:
        from handler import handle_message
        await handle_message(message)
    message.channel.send.assert_called_once_with("scam")
    mock_post.assert_not_called()


@pytest.mark.asyncio
async def test_burger_count_single():
    message = make_message("i love burger")
    with patch("handler.post_burger_count", new=AsyncMock()) as mock_post:
        from handler import handle_message
        await handle_message(message)
    mock_post.assert_called_once_with("testuser", 1)


@pytest.mark.asyncio
async def test_burger_count_multiple():
    message = make_message("burger burger burger")
    with patch("handler.post_burger_count", new=AsyncMock()) as mock_post:
        from handler import handle_message
        await handle_message(message)
    mock_post.assert_called_once_with("testuser", 3)


@pytest.mark.asyncio
async def test_burger_count_case_insensitive():
    message = make_message("BURGER Burger burger")
    with patch("handler.post_burger_count", new=AsyncMock()) as mock_post:
        from handler import handle_message
        await handle_message(message)
    mock_post.assert_called_once_with("testuser", 3)


@pytest.mark.asyncio
async def test_no_burger_no_post():
    message = make_message("hello world")
    with patch("handler.post_burger_count", new=AsyncMock()) as mock_post:
        from handler import handle_message
        await handle_message(message)
    mock_post.assert_not_called()


@pytest.mark.asyncio
async def test_unknown_command_no_reply():
    message = make_message("!unknown")
    with patch("handler.post_burger_count", new=AsyncMock()):
        from handler import handle_message
        await handle_message(message)
    message.channel.send.assert_not_called()
