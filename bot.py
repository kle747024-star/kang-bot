import discord
from discord.ext import commands
import os
import asyncio

def create_bot(name):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"✅ {name} đăng nhập: {bot.user}")

    return bot

async def start_bot(token, name):
    print(f"{name} TOKEN:", token)  # 🔥 debug token

    if not token:
        print(f"❌ {name} thiếu TOKEN")
        return

    bot = create_bot(name)

    try:
        await bot.start(token)
    except Exception as e:
        print(f"❌ {name} lỗi:", e)

async def main():
    await asyncio.gather(
        start_bot(os.getenv("TOKEN_1"), "Bot 1"),
        start_bot(os.getenv("TOKEN_2"), "Bot 2"),
        start_bot(os.getenv("TOKEN_3"), "Bot 3"),
        start_bot(os.getenv("TOKEN_4"), "Bot 4"),
    )

asyncio.run(main())
