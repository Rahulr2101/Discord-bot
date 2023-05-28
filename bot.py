import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is online. Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)


@bot.command()
async def remind(ctx, time, *, reminder):
    try:
        seconds = parse_time_to_seconds(time)
        if seconds:
            await asyncio.sleep(seconds)
            await ctx.author.send(f"Reminder: {reminder}")
            await ctx.send(f"{ctx.author.mention}, I have reminded you: {reminder}")
        else:
            await ctx.send("Invalid time format. Please use a valid format like 10s, 1m, 2h, etc.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


def parse_time_to_seconds(time):
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}

    amount = int(time[:-1])
    unit = time[-1]

    if unit in units:
        return amount * units[unit]
    else:
        return None



bot.run('YOUR_BOT_TOKEN')
