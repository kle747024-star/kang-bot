import discord
import asyncio

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
        bot1.start("TOKEN_1"),
        bot2.start("TOKEN_2"),
        bot3.start("TOKEN_3"),
        bot4.start("TOKEN_4"),
    )

asyncio.run(main())
