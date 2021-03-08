#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#
import time

from pyrogram import Client, filters
from presets import Presets


@Client.on_message(filters.private & filters.command(['start', 'help']))
async def help_me(bot, message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=Presets.WELCOME_TEXT.format(message.from_user.first_name)
    )

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    msg = await bot.send_message(
        chat_id=message.chat.id,
        text=Presets.BOT_PM_TEXT,
        reply_to_message_id=message.message_id
    )
    time.sleep(6)
    try:
        await msg.delete()
        await message.delete()
    except Exception:
        pass
