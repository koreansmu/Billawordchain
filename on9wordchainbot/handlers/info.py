import asyncio
import time
from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter, CommandHelp, CommandStart
from aiogram.utils.deep_linking import get_start_link
from aiogram.utils.markdown import quote_html

from .. import GlobalState, bot, dp
from ..constants import GameState
from ..utils import inline_keyboard_from_button, send_private_only_message
from ..words import Words


@dp.message_handler(CommandStart("help"), ChatTypeFilter([types.ChatType.PRIVATE]))
@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message) -> None:
    if message.chat.id < 0:
        await message.reply(
            "Please use this command in private.",
            allow_sending_without_reply=True,
            reply_markup=inline_keyboard_from_button(
                types.InlineKeyboardButton("Help message", url=await get_start_link("help"))
            )
        )
        return

    await message.reply(
        (
            "/gameinfo - Game mode descriptions\n"
            "/troubleshoot - Resolve common issues\n"
            "/reqaddword - Request addition of words\n"
            "/feedback - Send feedback to bot owner\n\n"
            "You may message [Jono](tg://user?id=463998526) "
            "in *English / Cantonese* if you have issues with the bot.\n"
            "Official Group: https://t.me/+T30aTNo-2Xx2kc52\n"
            "Word Additions Channel (with status updates): @on9wcwa\n"
            "Source Code: [jonowo/on9wordchainbot](https://github.com/jonowo/on9wordchainbot)\n"
            "Epic icon designed by [Adri](tg://user?id=303527690)"
        ),
        allow_sending_without_reply=True
    )


@dp.message_handler(commands="gameinfo")
@send_private_only_message
async def cmd_gameinfo(message: types.Message) -> None:
    await message.reply(
        (
            "/startclassic - Cʟᴀsɪᴄ ɢᴀᴍᴇ\n"
            "ᴘʟᴀʏᴇʀs ᴛᴀᴋᴇ ᴛᴜʀɴs ᴛᴏ sᴇɴᴅ ᴡᴏʀᴅs sᴛᴀʀᴛɪɴɢ ᴡɪᴛʜ ᴛʜᴇ ʟᴀsᴛ ʟᴇᴛᴛᴇʀ ᴏғ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜs ᴡᴏʀᴅ.\n\n"
            "Vᴀʀɪᴀɴᴛs:\n"
            "/starthard - Hᴀʀᴅ ᴍᴏᴅᴇ ɢᴀᴍᴇ\n"
            "/startrandom - Rᴀɴᴅᴏᴍ Tᴜʀɴ Oʀᴅᴇʀ ɢᴀᴍᴇ\n"
            "/startcfl - Cʜᴏsᴇɴ ғɪʀsᴛ ʟᴇᴛᴛᴇʀ ɢᴀᴍᴇ\n"
            "/startrfl - Rᴀɴᴅᴏᴍ ғɪʀsᴛ ʟᴇᴛᴛᴇʀ ɢᴀᴍᴇ\n"
            "/startbl - Bᴀɴɴᴇᴅ ʟᴇᴛᴛᴇʀs ɢᴀᴍᴇ\n"
            "/startrl - Rᴇǫᴜɪʀᴇᴅ ʟᴇᴛᴛᴇʀ ɢᴀᴍᴇ\n\n"
            "/startelim - Eʟɪᴍɪɴᴀᴛɪᴏɴ ɢᴀᴍᴇ\n"
            "ᴇᴀᴄʜ ᴘʟᴀʏᴇʀ's sᴄᴏʀᴇ ɪs ᴛʜᴇɪʀ ᴄᴜᴍᴜʟᴀᴛɪᴠᴇ ᴡᴏʀᴅ ʟᴇɴɢᴛʜ. "
            "ᴛʜᴇ ʟᴏᴡᴇsᴛ sᴄᴏʀɪɴɢ ᴘʟᴀʏᴇʀs ᴀʀᴇ ᴇʟɪᴍɪɴᴀᴛᴇᴅ ᴀғᴛᴇʀ ᴇᴀᴄʜ ʀᴏᴜɴᴅ.\ɴ\ɴ"
            "/sᴛᴀʀᴛᴍᴇʟɪᴍ - ᴍɪxᴇᴅ ᴇʟɪᴍɪɴᴀᴛɪᴏɴ ɢᴀᴍᴇ\ɴ"
            "ᴇʟɪᴍɪɴᴀᴛɪᴏɴ ɢᴀᴍᴇ ᴡɪᴛʜ ᴅɪғғᴇʀᴇɴᴛ ᴍᴏᴅᴇs. ᴛʀʏ ᴀᴛ ᴛʜᴇ [ᴏғғɪᴄɪᴀʟ ɢʀᴏᴜᴘ] (https://t.me/BillaCore)."
        ),
        allow_sending_without_reply=True
    )


@dp.message_handler(commands="troubleshoot")
@send_private_only_message
async def cmd_troubleshoot(message: types.Message) -> None:
    await message.reply(
        (
            "ᴛʜᴇsᴇ sᴛᴇᴘs ᴀssᴜᴍᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇs. "
            "ɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ, ᴘʟᴇᴀsᴇ ᴀsᴋ ᴀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴛᴏ ᴄʜᴇᴄᴋ ɪɴsᴛᴇᴀᴅ.\n\n"
            "<b>ɪғ ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇs ɴᴏᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ <code>/start[mode]</code></b>, check if:\n"
            "₁. ᴛʜᴇ ʙᴏᴛ ɪs ᴀʙsᴇɴᴛ ғʀᴏᴍ / ᴍᴜᴛᴇᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ "
            "\u27a1\ufe0f Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ / ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ʙᴏᴛ\n"
            "2. sʟᴏᴡ ᴍᴏᴅᴇmode ɪs ᴇɴᴀʙʟᴇᴅ \u27a1\ufe0f ᴅɪsᴀʙʟᴇ sʟᴏᴡ ᴍᴏᴅᴇ\n"
            "3. Sᴏᴍᴇᴏɴᴇ sᴘᴀᴍᴍᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ʏᴘᴜʀ ɢʀᴏᴜᴘ ʀᴇᴄᴇɴᴛʟʏ "
            "\u27a1\ufe0f ᴛʜᴇ ʙᴏᴛ ɪs ʀᴀᴛᴇ ʟɪᴍɪᴛᴇᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴡᴀɪᴛ ᴘᴀᴛɪᴇɴᴛʟʏ\n"
            "4. Tʜᴇ ʙᴏᴛ ᴅᴏᴇs ɴᴏᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ <code>/ping</code> "
            "\u27a1\ufe0f ʙɪʟʟᴀ ᴡᴏʀᴅ ᴄʜᴀɪɴ ᴍɪɢʜᴛ ʙᴇ ᴏғғ, ᴄʜᴇᴄᴋ @BillaCore ғᴏʀ sᴛᴀᴛᴜs ᴜᴘᴅᴀᴛᴇ\n\n"
            "<b>ɪғ ᴛʜᴇ ʙᴏᴛ ᴄᴀɴɴᴏᴛ ʙᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ</b>:\n"
            "1. ᴛʜᴇʀᴇ ᴄᴀɴ ʙᴇ ᴀᴛ ᴍᴏsᴛ 20 ʙᴏᴛs ɪɴ ᴀ ɢʀᴏᴜᴘ. ᴄʜᴇᴄᴋ ɪғ ᴛʜɪs ʟɪᴍɪᴛ ɪs ʀᴇᴀᴄʜᴇᴅ.\n\n"
            "ɪғ ʏᴏᴜ ᴇɴᴄᴏᴜɴᴛᴇʀ ᴏᴛʜᴇʀ ɪssᴜᴇs, ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ  ᴅᴇᴠʟᴏᴘᴇʀ <a href='tg://user?id=5960968099'>ᴍʏ ᴏᴡɴᴇʀ</a>."
        ),
        parse_mode=types.ParseMode.HTML,
        allow_sending_without_reply=True
    )


@dp.message_handler(commands="ping")
async def cmd_ping(message: types.Message) -> None:
    t = time.time()
    msg = await message.reply("Pong!", allow_sending_without_reply=True)
    await msg.edit_text(f"Pong! `{time.time() - t:.3f}s`")


@dp.message_handler(commands="chatid")
async def cmd_chatid(message: types.Message) -> None:
    await message.reply(f"`{message.chat.id}`", allow_sending_without_reply=True)


@dp.message_handler(commands="runinfo")
async def cmd_runinfo(message: types.Message) -> None:
    build_time_str = (
        "{0.day}/{0.month}/{0.year}".format(GlobalState.build_time)
        + " "
        + str(GlobalState.build_time.time())
        + " HKT"
    )
    uptime = datetime.now().replace(microsecond=0) - GlobalState.build_time
    await message.reply(
        (
            f"Build time: `{build_time_str}`\n"
            f"Uptime: `{uptime.days}.{str(uptime).rsplit(maxsplit=1)[-1]}`\n"
            f"Words in dictionary: `{Words.count}`\n"
            f"Total games: `{len(GlobalState.games)}`\n"
            f"Running games: `{len([g for g in GlobalState.games.values() if g.state == GameState.RUNNING])}`\n"
            f"Players: `{sum(len(g.players) for g in GlobalState.games.values())}`"
        ),
        allow_sending_without_reply=True
    )


@dp.message_handler(is_owner=True, commands="playinggroups")
async def cmd_playinggroups(message: types.Message) -> None:
    if not GlobalState.games:
        await message.reply("No groups are playing games.", allow_sending_without_reply=True)
        return

    groups = []

    async def append_group(group_id: int) -> None:
        try:
            group = await bot.get_chat(group_id)
            url = await group.get_url()
            # TODO: weakref exception is aiogram bug, wait fix
        except TypeError as e:
            if str(e) == "cannot create weak reference to 'NoneType' object":
                text = "???"
            else:
                text = f"(<code>{e.__class__.__name__}: {e}</code>)"
        except Exception as e:
            text = f"(<code>{e.__class__.__name__}: {e}</code>)"
        else:
            if url:
                text = f"<a href='{url}'>{quote_html(group.title)}</a>"
            else:
                text = f"<b>{group.title}</b>"

        if group_id not in GlobalState.games:  # In case the game ended during API calls
            return

        groups.append(
            text + (
                f" <code>{group_id}</code> "
                f"{len(GlobalState.games[group_id].players_in_game)}/{len(GlobalState.games[group_id].players)}P "
                f"{GlobalState.games[group_id].turns}W "
                f"{GlobalState.games[group_id].time_left}s"
            )
        )

    await asyncio.gather(*[append_group(gid) for gid in GlobalState.games])
    await message.reply(
        "\n".join(groups), parse_mode=types.ParseMode.HTML,
        allow_sending_without_reply=True
    )
