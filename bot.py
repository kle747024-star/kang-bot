import discord
import asyncio
import os

intents = discord.Intents.default()

bot1 = discord.Client(intents=intents)
bot2 = discord.Client(intents=intents)
bot3 = discord.Client(intents=intents)
bot4 = discord.Client(intents=intents)

@bot1.event
async def on_ready():
    print(f"Bot 1: {bot1.user}")

@bot2.event
async def on_ready():
    print(f"Bot 2: {bot2.user}")

@bot3.event
async def on_ready():
    print(f"Bot 3: {bot3.user}")

@bot4.event
async def on_ready():
    print(f"Bot 4: {bot4.user}")

async def main():
    await asyncio.gather(
        bot1.start(os.getenv("TOKENKANG")),
        bot2.start(os.getenv("TOKENBONG")),
        bot3.start(os.getenv("TOKENTHAO")),
        bot4.start(os.getenv("TOKENNAM")),
    )

asyncio.run(main())
