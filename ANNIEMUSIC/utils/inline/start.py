from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from ANNIEMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🗒 Command", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="💫 sᴜᴘᴘᴏʀᴛ 💫"", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="💫 sᴜᴘᴘᴏʀᴛ 💫", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="🍬 ᴄʜᴀɴɴᴇʟ 🍬", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="🗒 Command", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons


def music_start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="+ Add me to your clan darlo +",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🗒 Command", callback_data="feature"),
        ],
        [
            InlineKeyboardButton(text="✨ ᴏᴡɴᴇʀ ✨", callback_data="developer"),
            InlineKeyboardButton(text="🍬 ᴄʜᴀɴɴᴇʟ 🍬", url="https://t.me/ToluUpdate"),
        ],
    ]
    return buttons
    
