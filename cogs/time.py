import discord
from discord.ext import commands
import asyncio
from datetime import datetime
# from reminder.reminder import Reminder



class Remind(commands.Cog):

	def __init__(self,bot):
		self.bot = bot
		self.reminders = {}

	@commands.command()
	async def remind(self,ctx,*args):

		try:
			duration = 60*(int(args[0])*60 + int(args[1]))
			phrase = ''
			for i in range(len(args)):
				if i>=2:
					phrase = phrase + args[i] + ' '
			embed = discord.Embed(
			description = "Reminder set for {hr} hours and {min} minutes from now.".format(hr = args[0], min = args[1]),
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
			await ctx.send(embed = embed)
			
			# using the user as the dictionary key, add reminder to list
			# each reminder will be its own dictionary, with an index, 
			if ctx.message.author not in self.reminders:
				self.reminders[ctx.message.author] = []

			start = datetime.now()

			reminder = Reminder(phrase,duration,start,ctx.message.id)
			self.reminders[ctx.message.author].append(reminder)


			await asyncio.sleep(duration)

			# check if reminder still in list

			if reminder in self.reminders[ctx.message.author]:

				embed = discord.Embed(
				description = phrase,
				colour = discord.Colour.from_rgb(178, 107, 209)
				)

				await ctx.message.author.send(embed = embed)
				self.reminders[ctx.message.author].remove(reminder)
			
		except:
			embed = discord.Embed(
			description = "Improper Usage\n__**Reminder**__\nFirst argument is the number of hours until reminder is sent.\nSecond argument is the number of minutes until reminder is sent.\n"\
				+ 'All following arguments is the message to be sent.\n__**Usage Example**__\n&reminder 1 30 do homework\n(sends the user the message "do homework" after 1 hour 30 minutes)',
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
			await ctx.send(embed = embed)


	@commands.command()
	async def reminders(self,ctx,*args):
		# reminder = {ctx.message.id:[phrase,duration,start]}
		embed = discord.Embed(
		colour = discord.Colour.from_rgb(178, 107, 209)
		)
		try:
			if args[0] == 'clear':
				self.reminders[ctx.message.author] = []
				embed.add_field(name = "Reminders", value = "No reminders.",inline = False)
				await ctx.send(embed = embed)
		except:
			try:
				if not self.reminders[ctx.message.author]:
					embed.add_field(name = "Reminders", value = "No reminders.",inline = False)
					await ctx.send(embed = embed)
				else:
					now = datetime.now()
					for reminder in self.reminders[ctx.message.author]:
						embed.add_field(name = "Reminder", value = reminder.check(now),inline = False)
					await ctx.send(embed = embed)
			except:
				embed.add_field(name = "Error", value = "No reminders.",inline = False)
				await ctx.send(embed = embed)


class Reminder:

	def __init__(self,phrase,duration,start,ID = None):
		self.phrase = phrase
		self.duration = duration
		self.start = start
		try:
			self.id = ID
		except:
			self.id = -1

	def check(self,now):
		passed = now - self.start
		remaining = int(self.duration - passed.total_seconds())
		if remaining > 0:
			hrs = remaining//3600
			mins = remaining//60 - 60*hrs
			secs = remaining - 3600*hrs - 60*mins
			if hrs == 0:
				if mins ==0:
					wait = f"{secs} seconds"
				else:
					wait = f"{mins} minutes {secs} seconds"
			else:
				wait = f"{hrs} hours {mins} minutes {secs} seconds"
		else:
			wait = "Reminder has passed"
		
		# message = f"Reminder: {self.phrase}\nTime Remaining: {wait}\n"
		message = f"Message: {self.phrase}\nTime Remaining: {wait}\n"
		return message



def setup(sushi):
	sushi.add_cog(Remind(sushi))