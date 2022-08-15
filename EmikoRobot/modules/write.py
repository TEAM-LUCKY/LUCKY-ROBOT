import requests
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from EmikoRobot import pbot as fallen


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [ʟᴜᴄᴋʏ'xᴅ](https://t.me/ramdimusicbot)
🥀 **ʀᴇQ ʙʏ:** {message.from_user.mention}
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ •",
                            url=f"https://t.me/ramdimusicbot?startgroup=new",
                        )
                    ]
                ]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [ʟᴜᴄᴋʏ'xᴅ](https://t.me/ramdimusicbot)
🥀 **ʀᴇQ ʙʏ :** {message.from_user.mention}
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ •",
                            url=f"https://t.me/ramdimusicbot?startgroup=new",
                        )
                    ]
                ]
            ),
        )


__mod_name__ = "𝚆ʀɪᴛᴇ 💘"

__help__ = """

 /write  : *» ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ...*

/awrite  : *» ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ... ʙᴇᴛᴀ*
 """
