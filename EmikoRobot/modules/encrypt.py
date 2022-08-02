from EmikoRobot import telethn as tbot
import os
from EmikoRobot.events import register
import secureme


@register(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        cmd = lel.text
    else:
        cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)


@register(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        ok = lel.text
    else:
        ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)


__mod_name__ = "Cᴏɴᴠᴛ ♻️"

__help__ = """
❂ /encrypt: ᴇɴᴄʀʏᴘᴛꜱ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ

❂ /decrypt: ᴅᴇᴄʀʏᴘᴛꜱ ᴘʀᴇᴠɪᴏᴜꜱʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ

❂ /zip: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟʏᴇ ᴛo ᴄᴏᴍᴘʀᴇꜱꜱ ɪᴛ ɪɴ .ᴢɪᴘ ғᴏʀᴍᴀᴛ

❂ /unzip: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴛᴏ ᴅᴇᴄᴏᴍᴘʀᴇꜱꜱ ɪᴛ ғʀᴏᴍ ᴛʜᴇ .ᴢɪᴘ ғᴏʀᴍᴀᴛ

*➻ ᴘᴏᴡᴇʀᴅ  ʙʏ © @Cute_Boy701 ™*
"""
