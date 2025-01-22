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
            "/gameinfo - Gᴀᴍᴇ Mᴏᴅᴇ Dᴇsᴄʀɪᴘᴛɪᴏɴs\n"
            "/troubleshoot - Rᴇsᴏʟᴠᴇ Cᴏᴍᴍᴏɴ Issᴜᴇs\n"
            "/reqaddword - Rᴇǫᴜᴇsᴛ Aᴅᴅɪᴛɪᴏɴ Oғ Wᴏʀᴅs\n"
            "/feedback - Sᴇɴᴅ Fᴇᴇᴅʙᴀᴄᴋ Tᴏ Bᴏᴛ Oᴡɴᴇʀ\n\n"
            "Yᴏᴜ Mᴀʏ Dᴍ [Sᴛᴇʟʟᴀʀ](tg://user?id=5960968099) "
            "In *English / Mysterious* Iғ Yᴏᴜ Hᴀᴠᴇ Issᴜᴇs Wɪᴛʜ Tʜᴇ Bᴏᴛ.\n"
            "Oғғɪᴄɪᴀʟ Gʀᴏᴜᴘ: https://t.me/Harmony_hub8\n"
            "Wᴏʀᴅ Aᴅᴅɪᴛɪᴏɴ Cʜᴀɴɴᴇʟ / Gᴄ (Sᴛᴀᴛᴜs  Uᴘᴅᴀᴛᴇs): @BillaCore\n"
            "Sᴏᴜʀᴄᴇ Cᴏᴍᴍᴜɴɪᴛʏ: [jonowo/on9wordchainbot](https://t.me/storm_core)\n"
            "Eᴘɪᴄ Iᴄᴏɴ Dᴇsɪɢɴᴇᴅ Bʏ [Kᴇxx](tg://user?id=6257927828)"
        ),
        allow_sending_without_reply=True
    )


@dp.message_handler(commands="gameinfo")
@send_private_only_message
async def cmd_gameinfo(message: types.Message) -> None:
    await message.reply(
        (
            "/startclassic - Cʟᴀsɪᴄ Gᴀᴍᴇ\n"
            "Pʟᴀʏᴇʀs Tᴀᴋᴇ Tᴜʀɴs Tᴏ Sᴇɴᴅ Wᴏʀᴅs Sᴛᴀʀᴛɪɴɢ Wɪᴛʜ Tʜᴇ Lᴀsᴛ Lᴇᴛᴛᴇʀ Oғ Tʜᴇ Pʀᴇᴠɪᴏᴜs Wᴏʀᴅ.\n\n"
            "Vᴀʀɪᴀɴᴛs:\n"
            "/starthard - Hᴀʀᴅ Mᴏᴅᴇ Gᴀᴍᴇ\n"
            "/startrandom - Rᴀɴᴅᴏᴍ Tᴜʀɴ Oʀᴅᴇʀ Gᴀᴍᴇ\n"
            "/startcfl - Cʜᴏsᴇɴ Fɪʀsᴛ Lᴇᴛᴛᴇʀ Gᴀᴍᴇ\n"
            "/startrfl - Rᴀɴᴅᴏᴍ Fɪʀsᴛ Lᴇᴛᴛᴇʀ Gᴀᴍᴇ\n"
            "/startbl - Bᴀɴɴᴇᴅ Lᴇᴛᴛᴇʀs Gᴀᴍᴇ\n"
            "/startrl - Rᴇǫᴜɪʀᴇᴅ Lᴇᴛᴛᴇʀ Gᴀᴍᴇ\n\n"
            "/startelim - Eʟɪᴍɪɴᴀᴛɪᴏɴ Gᴀᴍᴇ\n"
            "Eᴀᴄʜ Pʟᴀʏᴇʀ's Sᴄᴏʀᴇ Is Tʜᴇɪʀ Cᴜᴍᴜʟᴀᴛɪᴠᴇ Wᴏʀᴅ Lᴇɴɢᴛʜ. "
            "Tʜᴇ Lᴏᴡᴇsᴛ Sᴄᴏʀɪɴɢ Pʟᴀʏᴇʀs Aʀᴇ Eʟɪᴍɪɴᴀᴛᴇᴅ Aғᴛᴇʀ Eᴀᴄʜ Rᴏᴜɴᴅ.\n\n"
            "/startmelim - Mɪxᴇᴅ Eʟɪᴍɪɴᴀᴛɪᴏɴ Gᴀᴍᴇ\n"
            "Eʟɪᴍɪɴᴀᴛɪᴏɴ Gᴀᴍᴇ Wɪᴛʜ Dɪғғᴇʀᴇɴᴛ Mᴏᴅᴇs. Tʀʏ Aᴛ Tʜᴇ [Oғғɪᴄɪᴀʟ Gʀᴏᴜᴘ] (https://t.me/BillaCore)."
        ),
        allow_sending_without_reply=True
    )


@dp.message_handler(commands="troubleshoot")
@send_private_only_message
async def cmd_troubleshoot(message: types.Message) -> None:
    await message.reply(
        (
            "Tʜᴇsᴇ Sᴛᴇᴘs Assᴜᴍᴇ Yᴏᴜ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟᴇɢᴇs. "
            "Iғ Yᴏᴜ Dᴏ Nᴏᴛ, Pʟᴇᴀsᴇ Asᴋ A Gʀᴏᴜᴘ Aᴅᴍɪɴ Tᴏ Cʜᴇᴄᴋ Iɴsᴛᴇᴀᴅ.\n\n"
            "<b>ɪғ Tʜᴇ Bᴏᴛ Dᴏᴇs Nᴏᴛ Rᴇsᴘᴏɴᴅ Tᴏ <code>/start[mode]</code></b>, check if:\n"
            "₁. Tʜᴇ Bᴏᴛ Is Aʙsᴇɴᴛ Fʀᴏᴍ / Mᴜᴛᴇᴅ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ "
            "\u27a1\ufe0f Aᴅᴅ Tʜᴇ Bɪʟʟᴀ Wᴏʀᴅ Cʜᴀɪɴ Bᴏᴛ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ / Uɴᴍᴜᴛᴇ Tʜᴇ Bᴏᴛ\n"
            "2. Sʟᴏᴡ Mᴏᴅᴇ Is Eɴᴀʙʟᴇᴅ \u27a1\ufe0f Dɪsᴀʙʟᴇ Sʟᴏᴡ Mᴏᴅᴇ\n"
            "3. Sᴏᴍᴇᴏɴᴇ Sᴘᴀᴍᴍᴇᴅ Cᴏᴍᴍᴀɴᴅs Iɴ YOᴜʀ Gʀᴏᴜᴘ Rᴇᴄᴇɴᴛʟʏ "
            "\u27a1\ufe0f Tʜᴇ Bᴏᴛ Is Rᴀᴛᴇ Lɪᴍɪᴛᴇᴅ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ, Wᴀɪᴛ Pᴀᴛɪᴇɴᴛʟʏ\n"
            "4. Tʜᴇ Bᴏᴛ Dᴏᴇs Nᴏᴛ Rᴇsᴘᴏɴᴅ Tᴏ <code>/ping</code> "
            "\u27a1\ufe0f Bɪʟʟᴀ Wᴏʀᴅ Cʜᴀɪɴ Mɪɢʜᴛ Bᴇ Oғғ, Cʜᴇᴄᴋ @BillaCore Fᴏʀ Sᴛᴀᴛᴜs ᴜᴘᴅᴀᴛᴇ\n\n"
            "<b>Iғ Tʜᴇ Bᴏᴛ Cᴀɴɴᴏᴛ Bᴇ Aᴅᴅᴇᴅ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ</b>:\n"
            "1. Tʜᴇʀᴇ Cᴀɴ Bᴇ Aᴛ Mᴏsᴛ 20 Bᴏᴛs Iɴ A Gʀᴏᴜᴘ. Cʜᴇᴄᴋ Iғ Tʜɪs Lɪᴍɪᴛ Is Rᴇᴀᴄʜᴇᴅ.\n\n"
            "Iғ Yᴏᴜ Eɴᴄᴏᴜɴᴛᴇʀ Oᴛʜᴇʀ Issᴜᴇs, Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ  Dᴇᴠʟᴏᴘᴇʀ <a href='tg://user?id=5960968099'>Mʏ Oᴡɴᴇʀ</a>."
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
