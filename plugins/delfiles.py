#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

import os
import time

from bot import Bot
from presets import Presets
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from helper.get_messages import get_messages
from helper.custom_filter import allowed_chat_filter
from pyrogram.errors import ChatAdminRequired

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

@Bot.on_message(filters.command('cleanchat') & allowed_chat_filter)
async def del_all_command_fn(client: Bot, message: Message):
    if message.from_user.id not in Config.AUTH_USERS:
        await message.delete()
        return
    await message.delete()
    info = await client.get_me()
    try:
        status_message = await client.send_message(
            chat_id=message.chat.id,
            text=Presets.CLEAN_CHAT_MSG
        )
    except ChatAdminRequired:
        status_message = None
    try:
        await get_messages(
            client.USER,
            message.chat.id,
            0,
            status_message.message_id if status_message else message.message_id,
            []
        )
    except FloodWait as e:
        time.sleep(e.x)
    msg = await client.send_message(
        chat_id=message.chat.id,
        text=Presets.MSG_FOR_PIN.format(info.username, info.username)
    )
    await msg.pin()
