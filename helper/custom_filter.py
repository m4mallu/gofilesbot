#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

from pyrogram import filters
from pyrogram.types import Message


async def allowed_chat_filter_fn(_, __, m: Message):
    return bool(m.chat and m.chat.type in {"supergroup"})


allowed_chat_filter = filters.create(allowed_chat_filter_fn)
