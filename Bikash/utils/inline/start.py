from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ❱ 💥",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💖", url="https//t.me/dangerous_fighter_clan_0"
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url="https//t.me/timepassgroup01"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐇𝐞𝐥𝐩 💖", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💥", url="https//t.me/dangerous_fighter_clan_0"
            ),
            InlineKeyboardButton(
                text="🥀 𝐆𝐫𝐨𝐮𝐩 💥", url="https//t.me/timepassgroup01"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ 𝐎𝐰𝐧𝐞𝐫 ♕", url="https//t.me/taitangamerz"
            )
        ]
     ]
    return buttons
