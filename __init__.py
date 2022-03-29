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

from pyrogram import Client, idle
from app.config import Config

logger = logging.getLogger("app")
clients = []
success = 0
failure = 0

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins={"root":"app/plugins"}
)

async def RunClients(SESSIONS, API_ID, API_HASH, BOT, CHAT_ID):
    for SESSION in SESSIONS:
        clients.append(Client(SESSION, api_id=API_ID, api_hash=API_HASH))

    await BOT.start()
    for i in range(len(client)):
        for client in clients:
            try:
                await client.start()
                success += 1
                for chat in CHAT_ID:
                    return await bot.send_message(chat, f"[SUCCESS] - Started the Client of ID `{(await client.get_me()).id}`")

            except Exception as error:
                failure += 1
                logger.error(error)
                for chat in CHAT_ID:
                    return await bot.send_message(chat, f"[ERROR] - Failed to Start the Client {i} - {str(error)}")
    
    for chat in CHAT_ID:
        return await bot.send_message(chat, f"[STATUS] - Successfully Started {success} accounts\nFailed to Start {failure} accounts")

    await idle()

async def StopClients(SESSIONS, API_ID, API_HASH, BOT, CHAT_ID):
    for i in range(len(client)):
        for client in clients:
            try:
                await client.stop()
                for chat in CHAT_ID:
                    return await bot.send_message(chat, f"[SUCCESS] - Stopped the Client {i}")

            except Exception as error:
                for chat in CHAT_ID:
                    return await bot.send_message(chat, f"[ERROR] - Failed to Stop the Client {i} - {str(error)}")
    
    await BOT.stop()