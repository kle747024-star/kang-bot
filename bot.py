import discord
from discord.ext import commands
import os
import asyncio

def create_bot():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Đã đăng nhập: {bot.user}")

    return bot

async def start_bot(token):
    bot = create_bot()
    await bot.start(token)

async def main():
    tokens = [
        os.getenv("TOKEN_1"),
        os.getenv("TOKEN_2"),
        os.getenv("TOKEN_3"),
        os.getenv("TOKEN_4"),
    ]

    await asyncio.gather(*(start_bot(t) for t in tokens if t))

asyncio.run(main())
