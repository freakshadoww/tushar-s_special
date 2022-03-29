# Telegram LOTP - Listener for Telegram One Time Password
# Copyright (C) 2022 Jayant Hegde Kageri <https://github.com/jayantkageri>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from app import bot, clients
from app.config import Config
from pyrogram import filters

for i in range(len(clients)):
    for client in clients:
        @client.on_message(~filters.edited & filters.incoming)
        async def task(c, message):
            if message.from_user.id != 777000:
                if message.chat.id in Config.CHAT_ID and message.text.lower().startswith("/start"):
                    return await message.reply_text(f"[STATUS] - BOT {i} IS RUNNING FUNCTIONALLY")
                return
            text = message.text.split(" ").strip()
            if text[0].lower() == "login":
                code = text[3]
                mode = "TELEGRAM LOGIN"
            elif text[0].lower() == "web":
                code = message.text.split(":").strip()[0]
                mode = "WEB LOGIN"
            for chat in config.CHAT_ID:
                return await bot.send_message(chat, f"`{(await c.get_me()).id}` - {mode} CODE - `{code}`")