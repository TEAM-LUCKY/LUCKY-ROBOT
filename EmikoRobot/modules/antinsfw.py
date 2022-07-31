from os import remove

from pyrogram import filters

from EmikoRobot import pbot, arq, BOT_USERNAME as bn
from EmikoRobot.utils.errors import capture_err
from EmikoRobot.utils.permissions import adminsOnly
from EmikoRobot.ex_plugins.dbfunctions import is_nsfw_on, nsfw_off, nsfw_on

__mod_name__ = "Aɴᴛɪ-ɴꜱꜰᴡ​"

__help__ = """
*ᴀɴᴛɪ ᴘᴏʀɴ sʏsᴛᴇᴍ*

/antinsfw <oɴ> : ᴇɴᴀʙʟᴇᴅ ᴀɴᴛɪɴsғᴡ ᴀɴᴛɪᴘᴏʀɴ sʏsᴛᴇᴍ. ʙᴏᴛ ᴡɪʟʟ
                 ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs ᴄᴏɴᴛᴀɪɴɪɴɢ ɪɴᴀᴘᴘʀᴏᴘʀɪᴀᴛᴇ ᴄᴏɴᴛᴇɴᴛ ᴅᴇғᴇᴀᴛ ᴏɴ

/antinsfw <ᴏғғ> : sᴀʟᴇ ᴏғғ ʜɪ ǫ ᴋᴀʀ ɴᴀ ʙᴇ ᴏɴ ᴋᴀʀ ᴅᴇ

/scan : ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ/ᴅᴏᴄᴜᴍᴇɴᴛ/sᴛɪᴄᴋᴇʀ/ᴀɴɪᴍᴀᴛɪᴏɴ ᴛᴏ sᴄᴀɴ ɪᴛ

➻ *ᴘᴏᴡᴇʀᴅ  ʙʏ © @Cute_Boy701 ™*
"""


async def get_file_id_from_message(message):
    file_id = None
    if message.document:
        if int(message.document.file_size) > 3145728:
            return
        mime_type = message.document.mime_type
        if mime_type != "image/png" and mime_type != "image/jpeg":
            return
        file_id = message.document.file_id

    if message.sticker:
        if message.sticker.is_animated:
            if not message.sticker.thumbs:
                return
            file_id = message.sticker.thumbs[0].file_id
        else:
            file_id = message.sticker.file_id

    if message.photo:
        file_id = message.photo.file_id

    if message.animation:
        if not message.animation.thumbs:
            return
        file_id = message.animation.thumbs[0].file_id

    if message.video:
        if not message.video.thumbs:
            return
        file_id = message.video.thumbs[0].file_id
    return file_id


@pbot.on_message(
    (
        filters.document
        | filters.photo
        | filters.sticker
        | filters.animation
        | filters.video
    )
    & ~filters.private,
    group=8,
)
@capture_err
async def detect_nsfw(_, message):
    if not await is_nsfw_on(message.chat.id):
        return
    if not message.from_user:
        return
    file_id = await get_file_id_from_message(message)
    if not file_id:
        return
    file = await pbot.download_media(file_id)
    try:
        results = await arq.nsfw_scan(file=file)
    except Exception:
        return
    if not results.ok:
        return
    results = results.result
    remove(file)
    nsfw = results.is_nsfw
    if not nsfw:
        return
    try:
        await message.delete()
    except Exception:
        return
    await message.reply_text(
        f"""
**NSFW ɪᴍᴀɢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ & ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!**

**ᴜꜱᴇʀ:** {message.from_user.mention} [`{message.from_user.id}`]
**ꜱᴀꜰᴇ:** `{results.neutral} %`
**ᴘᴏʀɴ:** `{results.porn} %`
**ᴀᴅᴜʟᴛ:** `{results.sexy} %`
**ʜᴇɴᴛᴀɪ:** `{results.hentai} %`
**ᴅʀᴀᴡɪɴɢꜱ:** `{results.drawings} %`

__ᴜꜱᴇ `/antinsfw off` ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴛʜɪꜱ.__
"""
    )


@pbot.on_message(filters.command("scan"))
@capture_err
async def nsfw_scan_command(_, message):
    if not message.reply_to_message:
        await message.reply_text(
            "`Reply to an image/document/sticker/animation to scan it.`"
        )
        return
    reply = message.reply_to_message
    if (
        not reply.document
        and not reply.photo
        and not reply.sticker
        and not reply.animation
        and not reply.video
    ):
        await message.reply_text(
            "Reply to an image/document/sticker/animation to scan it."
        )
        return
    m = await message.reply_text("`Scanning...`")
    file_id = await get_file_id_from_message(reply)
    if not file_id:
        return await m.edit("`Something wrong happened...|")
    file = await pbot.download_media(file_id)
    try:
        results = await arq.nsfw_scan(file=file)
    except Exception:
        return
    remove(file)
    if not results.ok:
        return await m.edit(results.result)
    results = results.result
    await m.edit(
        f"""
**ɴᴇᴜᴛʀᴀʟ:** `{results.neutral} %`
**ᴘᴏʀɴ:** `{results.porn} %`
**ʜᴇɴᴛᴀɪ:** `{results.hentai} %`
**ꜱᴇxʏ:** `{results.sexy} %`
**ᴅʀᴀᴡɪɴɢꜱ:** `{results.drawings} %`
**ɴꜱꜰᴡ:** `{results.is_nsfw}`
"""
    )


@pbot.on_message(filters.command(["antinsfw", f"antinsfw@{bn}"]) & ~filters.private)
@adminsOnly("can_change_info")
async def nsfw_enable_disable(_, message):
    if len(message.command) != 2:
        await message.reply_text("ᴜꜱᴀɢᴇ: /antinsfw [on/off]")
        return
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "on" or status == "yes":
        await nsfw_on(chat_id)
        await message.reply_text(
            "ᴇɴᴀʙʟᴇᴅ ᴀɴᴛɪ-ɴꜱꜰᴡ ꜱʏꜱᴛᴇᴍ. ɪ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴄᴏɴᴛᴀɪɴɪɴɢ ɪɴᴀᴘᴘʀᴏᴘʀɪᴀᴛᴇ ᴄᴏɴᴛᴇɴᴛ."
        )
    elif status == "off" or status == "no":
        await nsfw_off(chat_id)
        await message.reply_text("ᴅɪꜱᴀʙʟᴇᴅ ᴀɴᴛɪ-ɴꜱꜰᴡ ꜱʏꜱᴛᴇᴍ.")
    else:
        await message.reply_text("ᴜɴᴋɴᴏᴡɴ ꜱᴜꜰꜰɪx, ᴜꜱᴇ /antinsfw [on/off]")
