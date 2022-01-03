import discord
from discord.ext import commands
from pymongo import MongoClient

bot = discord.Bot()



@bot.event
async def on_ready():
    print(f"{bot.user} has now logged in with ID {bot.user.id}!")

bot.run("token")

