import discord
import config
from discord.ext import commands

TOKEN = config.token

description = 'Cryptobot'
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    


@bot.command()
async def version():
    await bot.say(config.version)


@bot.command()
async def commandos():
    await bot.say('!version, !commands')

bot.run(TOKEN)
