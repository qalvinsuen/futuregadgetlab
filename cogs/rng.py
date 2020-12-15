import discord
from discord.ext import commands
import random

class RNG(commands.Cog):

	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def coinflip(self,ctx):
		flip = random.randint(0,1)
		if flip == 1:
			await ctx.send(":coin: HEADS")
		else:
			await ctx.send(":coin: TAILS")

	@commands.command()
	async def decide(self,ctx,*args):
		choices = []
		try:
			for arg in args:
				choices.append(arg)
			decision = random.choice(choices)
			await ctx.send(decision)
		except:
			await ctx.send('__**Decision**__\nRandomly makes a decision between given options.__\n**Usage Example**__\n&decide "ice cream" "chips" "pie"\n'\
				+'(randomly picks one of "ice cream", "chips", or "pie")')

	@commands.command()
	async def dice(self,ctx,*args):
		sides = [":one:",":two:",":three:",":four:",":five:",":six:"]
		try:
			num = int(args[0])
			results = ''
			if num > 300:
				await ctx.send("300 Dice Maximum")
			else:
				for i in range(0,num):
					roll = random.randint(0,5)
					results = results + sides[roll]
				await ctx.send(results)
		# except TypeError:
		# 	await ctx.send("**Dice**: Rolls *x* number of six-sided dice.\n**Usage Example**: &dice 10\n(*example rolls 10 dice*)")
		except:
			roll = random.randint(0,5)
			await ctx.send(sides[roll])

	@commands.command()
	async def rng(self,ctx,*args):
		try:
			a = int(args[0])
			b = int(args[1])
			roll = random.randint(a,b)
			embed = discord.Embed(colour = discord.Colour.from_rgb(178, 107, 209))
			embed.add_field(name = "RNG", value = f"{str(roll)}", inline = False)
			# await ctx.send("RNG: " + str(roll))
		except:
			a = int(args[0])
			roll = random.randint(0,a)
			await ctx.send("RNG: " + str(roll))




def setup(sushi):
	sushi.add_cog(RNG(sushi))