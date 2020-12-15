import discord
from discord.ext import commands
# import youtube_dl
import ffmpeg
import asyncio


# pip install playsound

# python -m pip install -U discord.py[voice]
# python -m pip install -U youtube_dl
# py -m pip install -U youtube_dl
# pip install ffmpeg


class Music(commands.Cog):

	def __init__(self,bot):
		self.players = {}
		self.sushi = bot

	@commands.command()
	async def join(self,ctx):
		channel = ctx.message.author.voice.channel
		await channel.connect()
		print("Voice Connected")

	@commands.command()
	async def disconnect(self,ctx):
		channel = ctx.voice_client.channel
		await ctx.voice_client.disconnect()
		print("Voice Disconnected")


	@commands.command()
	async def lovesong(self,ctx,member:discord.Member=None):
		if member == None:
			channel = ctx.message.author.voice.channel
		else:
			channel = member.voice.channel
		vc = await channel.connect()
		vc.play(discord.FFmpegPCMAudio(executable = "ffmpeg", source='01 Love Song.mp3'))
		# 01 Love Song.mp3
		duration = 260
		# 01. Anybody Have a Map_.mp3
		# duration = 150
		# 06. If I Could Tell Her.mp3
		print("Playing Love Song")
		await asyncio.sleep(duration)
		await ctx.voice_client.disconnect()


	@commands.command()
	async def kong(self,ctx,member:discord.Member=None):
		if member == None:
			channel = ctx.message.author.voice.channel
		else:
			channel = member.voice.channel
		vc = await channel.connect()
		vc.play(discord.FFmpegPCMAudio(source='Donkey Kong 64 - Ok.mp3'))
		print("Playing Donkey Kong OK")
		await asyncio.sleep(2)
		await ctx.voice_client.disconnect()


	@commands.command()
	async def bruh(self,ctx,member:discord.Member=None):
		if member == None:
			channel = ctx.message.author.voice.channel
		else:
			channel = member.voice.channel
		vc = await channel.connect()
		vc.play(discord.FFmpegPCMAudio(source='Bruh Sound Effect #2.mp3'))
		print("Playing Bruh")
		await asyncio.sleep(2)
		await ctx.voice_client.disconnect()


def setup(sushi):
	sushi.add_cog(Music(sushi))