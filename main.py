import discord
from discord.ext import commands
import os

name = input("UserName:")
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_connect():
    print("Cere140 Ai System online Logining as " + name)


@bot.command()
async def Start(ctx):
    await ctx.send("Hello am Ceres140 Ai system")

@bot.command()
async def Ceres140(ctx):
	await ctx.send("What Maye I do For You Master")

my_secret = os.environ['Token']
bot.run(my_secret)
