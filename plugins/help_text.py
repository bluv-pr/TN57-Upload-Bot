#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    update_channel = "https://t.me/TN57_BotZ"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("<b>Sorry You Are B a n n e d...!!! \n \nContact My Dev 👉 @BluVds To Resolve This Problem</b>")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**<b>Oh Dear In Order To Use Me Join My Update Channel 🤭</b>**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/TN57_BotZ")]
              ])
            )
            return
        else:
  
        await update.reply_text(Translation.HELP_USER.format(update.from_user.first_name),

        reply_to_message_id=update.message_id
    )
    return
    
    
@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def about(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source", url="https://github.com/X-Gorn/X-URL-Uploader"
                    ),
                    InlineKeyboardButton("Project Channel", url="https://t.me/xTeamBots"),
                ],
                [InlineKeyboardButton("Author", url="https://t.me/xgorn")],
            ]
        ),
        reply_to_message_id=update.message_id
    )



        
