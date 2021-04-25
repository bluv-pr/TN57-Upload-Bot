import os
import sqlite3
import logging
import pyrogram

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = loScretLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("WEBHOOK", False)):

    from sample_config import Config
else:
    from config import Config

from pyrogram import filters
from translation import Translation
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Clinton.on_message(filters.command(["start"]))
async def start(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Translation.START_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='⚜️ 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 ⚜️', url=f'https://t.me/TN57_BotZ'),
                                                 InlineKeyboardButton(text='⚜️ 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 ⚜️', url=f'https://t.me/TN57_BotZ') ],
                                               [ InlineKeyboardButton(text='ᴄʟᴏꜱᴇ', callback_data='DM') ] ] ) )



@Clinton.on_message(filters.command(["upgrade"]))
async def helpme(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Translation.UPGRADE_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='ᴄʟᴏꜱᴇ', callback_data='DM') ] ] ) )



@Clinton.on_message(filters.command(["about"]))
async def abot(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Translation.ABOUT_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='ᴄʟᴏꜱᴇ', callback_data='DM') ] ] ) )



@Clinton.on_message(filters.command(["bro"]))
async def upgra(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Translation.ABOUT_TEXT.
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='ᴄʟᴏꜱᴇ', callback_data='DM') ] ] ) )



@Clinton.on_callback_query()
async def button(bot, update):
 
      if  'DM'  in update.data:
                await update.message.delete()
