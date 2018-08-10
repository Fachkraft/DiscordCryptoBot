import discord
import datetime, time
import config
import crypto
import requests
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
    await bot.say('!commandos, !version, !btc, !obi')
    
@bot.command()
async def btc():
    await bot.say('Not yet implemented!')
    await bot.say('TO DO: Bitcoin price --> https://api.cryptowat.ch/markets/kraken/btceur/price')
    
@bot.command()
async def obi():
    await bot.say('Strong hands buds!')


@bot.command()
async def getCrypto():
	
	await bot.say(crypto.encryptedText)
	


bot.run(TOKEN)
