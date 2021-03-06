
from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from RocksMusicv3.helpers.decorators import authorized_users_only
from RocksMusicv3.helpers.decorators import errors
from RocksMusicv3.services.callsmusic import client as USER
from RocksMusicv3.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>๐๐๐ ๐ฆ๐ ๐๐ฌ ๐๐๐ฆ๐ข๐ง ๐จ๐ ๐ฒ๐จ๐ซ ๐ ๐ซ๐จ๐ฎ๐ฉ ๐๐ข๐ซ๐ฌ๐ญ</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "RocksMusicv3"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "**Jแดsแด แดสษชสส สสแด แดแดษชษด สแดสแดษด แดแดsษชแด แดสแดส แดแดสษดแดส แดสแด สแดษด...๐**")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>**Kแดษด แดส ษดแดแดแดสแดส แดแด สแดษขแดแดษด แดแดษชษด สแดสแดษด แดแดสสแดส sแดส สแดษด**๐</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>๐ ๐๐ฅ๐จ๐จ๐ ๐๐๐ข๐ญ ๐๐ซ๐ซ๐จ๐ซ ๐ \n User {user.first_name} ๐๐จ๐ฎ๐ฅ๐๐ง'๐ญ ๐ฃ๐จ๐ข๐ง ๐ฒ๐จ๐ฎ๐ซ ๐ ๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ ๐ญ๐จ ๐ก๐๐๐ฏ๐ฒ ๐ฃ๐จ๐ข๐ง ๐ซ๐๐ช๐ฎ๐๐ฌ๐ญ๐ฌ ๐๐จ๐ซ ๐ฎ๐ฌ๐๐ซ๐๐จ๐ญ! ๐๐๐ค๐ ๐ฌ๐ฎ๐ซ๐ ๐ฎ๐ฌ๐๐ซ ๐ข๐ฌ ๐ง๐จ๐ญ ๐๐๐ง๐ง๐๐ ๐ข๐ง ๐ ๐ซ๐จ๐ฎ๐ฉ. **Or To Contact @Dr_Asad_Ali**"
            "\n\nOr ๐ฆ๐๐ง๐ฎ๐๐ฅ๐ฅ๐ฒ ๐๐๐ ๐๐ฒ ๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐ญ๐จ ๐ฒ๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ง๐ ๐ญ๐ซ๐ฒ ๐๐ ๐๐ข๐ง</b>",
        )
        return
    await message.reply_text(
        "<b>**Mแดษชษด แดแด Gแดสแด**๐</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>๐๐ฌ๐๐ซ ๐๐จ๐ฎ๐ฅ๐๐ง'๐ญ ๐ฅ๐๐๐ฏ๐ ๐ฒ๐จ๐ฎ๐ซ ๐ ๐ซ๐จ๐ฎ๐ฉ! ๐๐๐ฒ ๐๐ ๐๐ฅ๐จ๐จ๐๐ฐ๐๐ข๐ญ๐ฌ."
            "\n\nOr ๐ฆ๐๐ง๐ฎ๐๐ฅ๐ฅ๐ฒ ๐ค๐ข๐๐ค ๐ฆ๐ ๐๐ซ๐จ๐ฆ ๐ญ๐จ ๐ฒ๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐๐๐๐ฏ๐ข๐ง๐  ๐๐ฅ๐ฅ ๐๐ก๐๐ญ๐ฌ")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐๐๐๐ฏ๐ข๐ง๐ ... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐๐๐๐ฏ๐ข๐ง๐ ... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("๐๐ฌ ๐๐ก๐๐ญ ๐๐ฏ๐๐ง ๐ฅ๐ข๐ง๐ค๐๐")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>๐๐๐ ๐ฆ๐ ๐๐ฌ ๐๐๐ฆ๐ข๐ง ๐จ๐ ๐ฒ๐จ๐ซ ๐๐ก๐๐ง๐ง๐๐ฅ ๐๐ข๐ซ๐ฌ๐ญ</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "RocksMusicv3"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "๐ ๐ฃ๐จ๐ข๐ง๐๐ ๐ก๐๐ซ๐ ๐๐ฌ ๐ฒ๐จ๐ฎ ๐ซ๐๐ช๐ฎ๐๐ฌ๐ญ๐๐")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>๐ก๏ธ๐๏ธ๐๏ธ๐๏ธ๐ข๏ธ ๐ก๐๐ฅ๐ฉ๐๐ซ ๐ฎ๐ฌ๐๐ซ๐๐จ๐ญ ๐ฃ๐จ๐ข๐ง๐๐ ๐ฒ๐จ๐ฎ๐ซ ๐๐ก๐๐ง๐ง๐๐ฅ</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>๐ ๐ญ๐๐๐๐ ๐พ๐๐๐ ๐ฌ๐๐๐๐ ๐ \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel, or contact to @Dr_Asad_Ali"
            "\n\nOr ๐ฆ๐๐ง๐ฎ๐๐ฅ๐ฅ๐ฒ ๐๐๐ ๐๐ฒ ๐๐ฌ๐ฌ๐ข๐ฌ๐ญ๐๐ง๐ญ ๐ญ๐จ ๐ฒ๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ง๐ ๐ญ๐ซ๐ฒ ๐๐ ๐๐ข๐ง</b>",
        )
        return
    await message.reply_text(
        "<b>๐ก๏ธ๐๏ธ๐๏ธ๐๏ธ๐ข๏ธ ๐ก๐๐ฅ๐ฉ๐๐ซ ๐ฎ๐ฌ๐๐ซ๐๐จ๐ญ ๐ฃ๐จ๐ข๐ง๐๐ ๐ฒ๐จ๐ฎ๐ซ ๐๐ก๐๐ง๐ง๐๐ฅ</b>",
    )
    
