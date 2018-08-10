import discord
import config
from discord.ext import commands

TOKEN = config.token

description = 'Cryptobot'
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.say("Type /commandos")


@bot.command()
async def version():
    await bot.say('0.0.1')


@bot.command()
async def commandos():
    await bot.say('!version, !commands')

bot.run(TOKEN)
