import io
import re
import html
import random
import requests
from EmikoRobot import dispatcher
from telegram import ParseMode, Update, Bot
from EmikoRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    truth = requests.get("https://elianaapi.herokuapp.com/games/truth").json()
    truth = truth.get("truth")
    update.effective_message.reply_text(truth)


def dare(update: Update, context: CallbackContext):
    args = context.args
    dare = requests.get("https://elianaapi.herokuapp.com/games/dares").json()
    dare = dare.get("dare")
    update.effective_message.reply_text(dare)


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__mod_name__ = "Tʀᴜᴛʜ 🎳"

__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
"""
