#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

import re
import os
import time

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from presets import Presets
from bot import Bot

if os.environ.get("ENV", False):
    from sample_config import Config
else:
    from config import Config

@Client.on_message(filters.group & filters.text)
async def query_mgs(client: Bot, message: Message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    query_message = message.text
    if len(message.text) > 2:
        for channel in Config.CHANNELS:
            async for messages in client.USER.search_messages(channel, query_message, filter="document"):
                filename = messages.document.file_name
                if re.search(rf'\b{query_message}\b', filename, re.IGNORECASE):
                    try:
                        await client.send_chat_action(
                            chat_id=message.from_user.id,
                            action="upload_video"
                        )
                    except Exception:
                        msg = await client.send_message(
                            chat_id=message.chat.id,
                            text=Presets.ASK_PM_TEXT,
                            reply_to_message_id=message.message_id
                        )
                        time.sleep(3)
                        await msg.delete()
                        await message.delete()
                        return
                    try:
                        await client.copy_message(
                            chat_id=message.from_user.id,
                            from_chat_id=messages.chat.id,
                            message_id=messages.message_id,
                            caption=Presets.CAPTION_TEXT
                        )
                    except FloodWait as e:
                        time.sleep(e.x)
