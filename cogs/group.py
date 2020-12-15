import discord
from discord.ext import commands
import random
import os

class Group(commands.Cog):


	def __init__(self,bot):
		self.bot = bot
		self.servers = []
		self.holders = []
		self.games = {}

	@commands.command()
	async def help(self,ctx,*args):
		try:
			embed = discord.Embed(
			title = "Future Gadget Lab Help",
			# title = "SushiBot Help",
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
			if args[0] == 'attack':
				embed.add_field(name = "Attack", value = "Attack @someone with your feelings stick.", inline = False)
			elif args[0] == 'blackjack':
				embed.add_field(name = "Blackjack", value = 'Start a game of Blackjack: "hit" to hit and "stand" to stand.', inline = False)
			elif args[0] == 'coinflip':
				embed.add_field(name = "Coinflip", value = "Flips a coin and returns heads or tails.", inline = False)
			elif args[0] == 'decide':
				embed.add_field(name = "Decision", value = 'Randomly makes a decision between given options.__\n**Usage Example**__\n&decide "ice cream" "chips" "pie"\n'\
					+'(randomly picks one of "ice cream", "chips", or "pie")', inline = False)
			elif args[0] == 'dice':
				embed.add_field(name = "Dice", value = "Rolls *x* number of six-sided dice.\n__**Usage Example**__\n&dice 10\n(*example rolls 10 dice*)", inline = False)
			elif args[0] == 'filter':
				embed.add_field(name = "Filters", value = "*blur, gray, edge, reflect, bright, 70s*\nUpload an image along with the command to apply the filter onto the uploaded image.\n__**Usage Example**__\n&filter edge", inline = False)
			elif args[0] == 'feelings':
				embed.add_field(name = "Feeling Stick", value = "Whoever holds the feelings stick has the right to express themselves without being judged.\nUses: `take` , `give @someone` , `holder` ", inline = False)
			elif args[0] == 'gordon':
				embed.add_field(name = "Gordon", value = "Sends an image of Gordon Ramsay telling you your argument is raw.\ne.g. &gordon sea bass", inline = False)
			elif args[0] == 'hangman':
				embed.add_field(name = "Hangman", value = "Starts a hangman game that anyone can participate in. Guess letters until you win or lose. " \
					+ "Takes an argument as the theme.\nThemes: `comics`, `fruits` , `house` , `pokemon` , `restaurant` , `animals` , `anime` , `eng`", inline = False)
			elif args[0] == 'poll':
				embed.add_field(name = "Poll", value = "Takes up to ten poll arguments and starts a poll with reactions to count votes.\n"\
					+ "If there is only one argument, the poll will have 👍 or 👎 reactions instead.\n"\
					+ "If your argument is a sentence, put it in quotes to have it count as one argument.\n"\
					+ 'e.g. &poll "This is one argument." "This is another"', inline = False)
			elif args[0] == 'remind':
				embed.add_field(name = "Remind", value = "First argument is the number of hours until reminder is sent.\nSecond argument is the number of minutes until reminder is sent.\n"\
					+ 'All following arguments is the message to be sent.\n__**Usage Example**__\n&remind 1 30 do homework\n(sends the user the message "do homework" after 1 hour 30 minutes)\n'\
					+ 'Use "&reminders" to see a list of your scheduled reminders.', inline = False)
			elif args[0] == 'reminders':
				embed.add_field(name = "Reminders", value = 'Returns a list of your reminders.\nSet reminders using the "&remind" command.', inline = False)
			elif args[0] == 'rng':
				embed.add_field(name = "RNG", value = "Use RNG with one number to generate a random number between 1 and that number, inclusive.\n"\
					+ "Use RNG with two numbers to generate a random number between those two numbers, inclusive.\n__**Usage Example**__\n&rng 8\n(generates a random number between 1 and 8)"\
					+ "\n&rng 3 27\n(generates a random number between 3 and 27", inline = False)
			elif args[0] == 'server':
				embed.add_field(name = "Server", value = "Returns the server name, the number of members in the server, and the server owner's name.", inline = False)
			elif args[0] == 'spongebob':
				embed.add_field(name = "Spongebob", value = "Sends an image of the spongebob mocking meme with text in the lower-uppercase meme format.\ne.g. &spongebob I'm the coolest", inline = False)
			# voice commands
			elif args[0] == 'bruh':
					embed.add_field(name = "bruh", value = 'Plays the "bruh" sound effect in your current voice channel or you can &bruh @someone if they are in a voice channel.', inline = False)
			elif args[0] == 'kong':
					embed.add_field(name = "Donkey Kong OK", value = 'Plays the Donkey Kong "OK" sound effect in your current voice channel or you can &kong @someone if they are in a voice channel.', inline = False)
			elif args[0] == 'lovesong':
					embed.add_field(name = "lovesong", value = 'Plays Love Song by Sara Bareilles in your current voice channel or you can &lovesong @someone if they are in a voice channel.', inline = False)
			await ctx.send(embed = embed)
		except:
			embed = discord.Embed(
			title = "SushiBot Help",
			description = "`Command Prefix: &`",
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
			embed.add_field(name = "Help", value = "`Type '&help' followed by a command for a description of the command's usage.`", inline = False)
			embed.add_field(name = "Example", value = "`&help dice\n(returns the description for the 'dice' command)`", inline = False)
			# embed.add_field(name = "Example", value = "&help dice\n(*returns the description for the 'dice' command*)", inline = False)
			embed.add_field(name = "Commands", value = "`attack` , `blackjack` , `bruh` , `coinflip` , `decide` , `dice` , `feelings` , `filter` , `gordon` , `hangman` , `kong` , `ping` , `lovesong` , `poll` , `remind` , `reminders` , `rng` , `server` , `spongebob` ", inline = False)
			await ctx.send(embed = embed)


	@commands.command()
	async def feelings(self, ctx, arg=None, member:discord.Member=None):
		if ctx.guild not in self.servers:
			self.servers.append(ctx.guild)
			self.holders.append(None)
		index = self.servers.index(ctx.guild)
		if arg == 'give':
			try:
				if self.holders[index] == ctx.message.author:
					await ctx.send(f"{ctx.message.author.mention} has given {member.mention} the feelings stick :magic_wand:.")
					self.holders[index] = member
				else:
					await ctx.send(f"You are not holding the feelings stick so you cannot give it to {member.mention}.")
			except:
				await ctx.send(f"You are not holding the feelings stick so you cannot give it to {member.mention}.")
		elif arg == 'take':
			self.holders[index] = ctx.message.author
			await ctx.send(f"{self.holders[index].mention} has the feelings stick :magic_wand:, let them speak without being judged.")
		elif arg == 'holder':
			try:
				await ctx.send(f"{self.holders[index].mention} is holding the feelings stick. :magic_wand:")
			except:
				await ctx.send("No one is holding the feelings stick.")
		else:
			await ctx.send("Whoever holds the feelings stick :magic_wand: has the permission to express themselves without being judged.")

	@commands.command()
	async def attack(self, ctx, member:discord.Member=None):
		try:
			index = self.servers.index(ctx.guild)
			if self.holders[index] == ctx.message.author:
				choices = ["attacks :fire::fire::fire:","stabs :knife::knife::knife:","punches :right_facing_fist::fist::left_facing_fist:","sharknados :shark::cloud_tornado::shark:",\
				"smites :zap::cloud_lightning::zap:","baguettes :french_bread::french_bread::french_bread:","snipes :bow_and_arrow::arrow_right::dart:","bombs :bomb::boom::firecracker:"]
				decision = random.choice(choices)
				await ctx.send(f"{ctx.message.author.mention} {decision} {member.mention} with the feelings stick :magic_wand:.")
		except:
			if member == None:
				await ctx.send("Select a target :face_with_monocle:")
			else:
				await ctx.send("Hitting people is illegal unless you have a feelings stick :magic_wand:.")
		

	@commands.command()
	async def poll(self,ctx, *args):
		numbers = ["\U00000031\U0000FE0F\U000020E3","\U00000032\U0000FE0F\U000020E3","\U00000033\U0000FE0F\U000020E3",\
			"\U00000034\U0000FE0F\U000020E3","\U00000035\U0000FE0F\U000020E3","\U00000036\U0000FE0F\U000020E3",\
			"\U00000037\U0000FE0F\U000020E3","\U00000038\U0000FE0F\U000020E3","\U00000039\U0000FE0F\U000020E3","\U0001F51F"]
		options = ''
		if len(args) > 1 and len(args)<=10:

			for i in range(len(args)):
				options = options + numbers[i] + ' ' + args[i] +'\n'
			embed = discord.Embed(
			title = "Poll",
			description = options,
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
			pollmsg = await ctx.send(embed = embed)	
			pollmsg
			for i in range(len(args)):
				await pollmsg.add_reaction(numbers[i])

		elif len(args) == 1:
			embed = discord.Embed(
			title = "Poll",
			description = f"{args[0]}",
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
			pollmsg = await ctx.send(embed = embed)
			pollmsg
			await pollmsg.add_reaction('👍')
			await pollmsg.add_reaction('👎')
		elif len(args) == 0:
			await ctx.send("Need at least one argument.")
		else:
			await ctx.send("Maximum number of poll options is ten.")

		

def setup(sushi):
	sushi.add_cog(Group(sushi))