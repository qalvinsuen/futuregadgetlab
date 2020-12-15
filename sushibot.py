# cmd in file explorer folder where the files are located
# git add .
# git commit -am "edit"
# git push heroku master
## turn off then turn on bot in heroku dashboard > resources
# heroku logs -a friedsushibot

# pip install -U python-dotenv

import discord
from discord.ext import commands
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from _io import BytesIO
import requests
import random
import asyncio
import os

# SUSHI_TOKEN for Fried Sushi Bot
# DISCORD_TOKEN for Future Gadget Lab
TOKEN = os.environ.get('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.members = True
sushi = commands.Bot(command_prefix="&", help_command=None, intents=intents)

@sushi.event
async def on_ready():
	await sushi.change_presence(activity=discord.Game(name=f"{len(sushi.guilds)} Servers | &help"))
	print("Sushi has been fried!")

@sushi.command()
async def load(ctx,extension):
	sushi.load_extension(f'cogs.{extension}')
@sushi.command()
async def unload(ctx,extension):
	sushi.unload_extension(f'cogs.{extension}')
@sushi.command()
async def reload(ctx,extension):
	sushi.unload_extension(f'cogs.{extension}')
	sushi.load_extension(f'cogs.{extension}')


@sushi.command()
async def hello(ctx):
	await ctx.send("Hi, how are you?")


@sushi.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(sushi.latency*1000)}ms')


@sushi.command()
async def server(ctx):
	embed = discord.Embed(
		# title = "Server Information",
		colour = discord.Colour.from_rgb(178, 107, 209)
		)
	embed.add_field(name = "Server Name", value = "{guildName}".format(guildName = ctx.guild.name), inline = False)
	embed.add_field(name = "Member Count", value = "{memberCount}".format(memberCount = ctx.guild.member_count), inline = False)
	embed.add_field(name = "Owner", value = "{owner}".format(owner = sushi.get_user(ctx.guild.owner_id)), inline = False)
	embed.add_field(name = "Description", value = f"{ctx.guild.description}", inline = False)
	embed.set_thumbnail(url=ctx.guild.icon_url)
	await ctx.send(embed = embed)



@sushi.event
async def on_message(message):
	if message.author == sushi.user:
		return
	elif 'lamb' in message.content.lower():
		await message.channel.send(file=discord.File('lambsauce.gif'))
	elif 'prrr' in message.content.lower():
		await message.channel.send(file=discord.File("prr.png"))
	elif 'zzz' in message.content.lower():
		await message.channel.send(file=discord.File("zzz.png"))
	await sushi.process_commands(message)


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		sushi.load_extension(f'cogs.{filename[:-3]}')


sushi.run(TOKEN)

