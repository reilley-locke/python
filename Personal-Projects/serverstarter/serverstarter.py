import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import subprocess

client = discord.Client(intents=discord.Intents.default())

#bot = Bot("!")
bot = commands.Bot(command_prefix='!',intents=discord.Intents.default())

@bot.command()
async def start(ctx):
    await ctx.send("Server is up!")
    subprocess.call([r'C:\Users\Rhloc\Desktop\RavenSMP\run.bat'])


@bot.command()
async def kill(ctx):
    await ctx.send('Shutting server down')
    print('stop')

bot.run('MTIyMjAzMjA5OTI0NzM5MDc3MQ.GNAzIp.zA9MjVEqT9DECMCa1YF58gtRSszkRyI6jAbtl0')