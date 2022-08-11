from telethon.errors.rpcerrorlist import YouBlockedUserError
from EmikoRobot import telethn as tbot
from EmikoRobot.events import register
from EmikoRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


__mod_name__ = "Sᴀɴɢᴍᴀᴛᴀ 🦋"

__help__ = """
*Sᴀɴɢᴍᴀᴛᴀ ɪɴꜰᴏ ʙᴏᴛ*

❂ /sg <ʀᴇᴘʟʏ>: ᴛᴏ ᴄʜᴇᴄᴋ ʜɪꜱᴛᴏʀʏ ɴᴀᴍᴇ
"""


@register(pattern="^/sg ?(.*)")
@register(pattern="^/check_name ?(.*)")
async def lastname(steal):
    steal.pattern_match.group(1)
    puki = await steal.reply("ʀᴇᴛʀɪᴇᴠɪɴɢ ꜱᴜᴄʜ ᴜꜱᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ..")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴍꜱɢ.")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ʀᴇᴀʟ ᴜꜱᴇʀꜱ ᴍꜱɢ")
        return
    await puki.edit("ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "ᴇʀʀᴏʀ, ʀᴇᴘᴏʀᴛ ᴛᴏ @TeraYaarHooMai"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                ) 
                return
            if response.text.startswith("ɴᴏ ʀᴇᴄᴏʀᴅꜱ") or r.text.startswith(
                "No records"
            ):
                await puki.edit("ɪ ᴄᴀɴᴛ ꜰɪɴᴅ ᴛʜɪꜱ ᴜꜱᴇʀ'ꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ, ᴛʜɪꜱ ᴜꜱᴇʀ ʜᴀꜱʜ ɴᴇᴠᴇʀ ᴄʜᴀɴɢᴇ ʜɪꜱ ɴᴀᴍᴇ ʙᴇꜰᴏʀᴇ.")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"{response.message}")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("ɪ ᴍ ꜱɪᴄᴋ ꜱᴏʀʀʏ..")
