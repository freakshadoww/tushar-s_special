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

from tgEasy.config import config

class Conifg:
    API_ID = config("API_ID")
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    SESSIONS = config("SESSIONS")
    if "," in config("CHAT_ID"):
        CHAT_ID = config("CHAT_ID").split(",").strip()
    else:
        CHAT_ID = [config("CHAT_ID")]