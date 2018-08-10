import discord
from discord.ext import commands

const version = '0.0.1'
TOKEN = 'CryptoBot_Token'

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.say("Type !commands")


@bot.command()
async def version():
    await bot.say(version)


@bot.command()
async def commands
    await bot.say("!version, !commands")

bot.run(TOKEN)
