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

import asyncio
import logging
from app import *
from app.config import Config

if __name__ == "__main__":
    try:
        asyncio.run(RunClients(Config.SESSIONS, Config.API_ID, Config.API_HASH, bot, Config.CHAT_ID))
    except Exception as error:
        logger.error(error)
    asyncio.run(StopClients(Config.SESSIONS, Config.API_ID, Config.API_HASH, bot, Config.CHAT_ID))