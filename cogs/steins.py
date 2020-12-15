import discord
from discord.ext import commands
import random
import os

class Steins(commands.Cog):


	def __init__(self,bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_message(self,message):
		content = message.content.lower()
		if message.author == self.bot.user:
			return


		# PNGs
		elif 'time' in content:
			await message.channel.send(file=discord.File("steins/time.png"))
		elif 'banana' in content:
			await message.channel.send(file=discord.File("steins/banana.png"))
		elif 'girls' in content or 'gurls' in content:
			await message.channel.send(file=discord.File("steins/girlslove.png"))
		elif 'secret' in content or 'tell us' in content:
			await message.channel.send(file=discord.File("steins/secrets.png"))
		elif 'training' in content:
			await message.channel.send(file=discord.File("steins/training.png"))
		elif 'trick' in content:
			await message.channel.send(file=discord.File("steins/tricks.png"))
		elif 'fap' in content or 'masturbate' in content:
			await message.channel.send(file=discord.File("steins/fap.png"))
		elif 'pocket' in content or 'masturbate' in content:
			await message.channel.send(file=discord.File("steins/handsinpockets.png"))
		elif 'stein' in content or 'choice' in content:
			await message.channel.send(file=discord.File("steins/choice.png"))
		

		# GIFs
		elif 'alone' in content or 'lonely' in content or 'talking to myself' in content or 'talking to yourself' in content:
			await message.channel.send(file=discord.File("steins/talking.gif"))
		elif ' perv' in content or 'hentai' in content or 'pervert' in content or content == 'perv':
			await message.channel.send(file=discord.File("steins/pervert.gif"))
		elif 'research' in content or 'pose' in content:
			await message.channel.send(file=discord.File("steins/research.gif"))
		elif 'tell me' in content or 'organization' in content:
			await message.channel.send(file=discord.File("steins/caught.gif"))
		elif 'lab coat' in content:
			await message.channel.send(file=discord.File("steins/labcoat.gif"))
		elif 'dr pepper' in content:
			await message.channel.send(file=discord.File("steins/drpepper.gif"))


# El Psy Kongroo
# I'm the great mad scientist, Hououin Kyoma!


		

def setup(sushi):
	sushi.add_cog(Steins(sushi))