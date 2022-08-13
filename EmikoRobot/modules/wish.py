import random

from telethon import events

from EmikoRobot import telethn as pbot


@pbot.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://telegra.ph/file/3fe0f7dedb81528a57313.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**ʜᴇʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱʜ ʙᴇᴇɴ ᴄᴀꜱᴛ.💜**\n\n__ᴄʜᴀɴᴄᴇ ᴏꜰ ꜱᴜᴄᴄᴇꜱꜱ {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://telegra.ph/file/3fe0f7dedb81528a57313.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**ʜᴇʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱʜ ʙᴇᴇɴ ᴄᴀꜱᴛ.💜**\n\n__ᴄʜᴀɴᴄᴇ ᴏꜰ ꜱᴜᴄᴄᴇꜱꜱ {mm}%__",
            reply_to=e,
        )
