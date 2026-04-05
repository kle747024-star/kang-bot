import discord
import asyncio

intents = discord.Intents.default()

# ===== BOT 1 =====
bot1 = discord.Client(intents=intents)

@bot1.event
async def on_ready():
    print(f"Bot 1 đã đăng nhập: {bot1.user}")

# ===== BOT 2 =====
bot2 = discord.Client(intents=intents)

@bot2.event
async def on_ready():
    print(f"Bot 2 đã đăng nhập: {bot2.user}")

# ===== BOT 3 (nếu cần) =====
bot3 = discord.Client(intents=intents)

@bot3.event
async def on_ready():
    print(f"Bot 3 đã đăng nhập: {bot3.user}")

# ===== CHẠY CÙNG LÚC =====
async def main():
    await asyncio.gather(
        bot1.start("TOKEN_1"),
        bot2.start("TOKEN_2"),
        bot3.start("TOKEN_3")  # có thể xoá nếu không dùng
    )

asyncio.run(main())
