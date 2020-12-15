import discord
from discord.ext import commands
import random

class BJGame:

	def __init__(self,user):
		cards = []
		for i in range(13):
			# spades
			cards.append([":spades:",(i+1)])
			# hearts
			cards.append([":hearts:",(i+1)])
			# clubs
			cards.append([":clubs:",(i+1)])
			# diamonds
			cards.append([":diamonds:",(i+1)])
		self.cardFace = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		self.cards = cards
		# player
		self.player = []
		self.ptotal = 0
		self.pstand = 0
		self.pstring = ''
		# dealer
		self.dealer = []
		self.dtotal = 0
		self.dstand = 0
		self.dstring = ''
		# board
		self.gameState = 1
		self.user = user.display_name
		self.board = f"{self.user}'s' Total: {self.ptotal}\nCards: [{self.pstring}]\n \nDealer's Total: {self.dtotal}\nCards: [{self.dstring}]"
		self.status = "**hit or stand**"
		

	def updateBoard(self,turn):
		if turn == 'player':
			self.ptotal = self.checkValue('player')
			self.pstring = ''
			for i in range(len(self.player)):
				if i == len(self.player) - 1:
					self.pstring = self.pstring + self.player[i][0] + self.cardFace[self.player[i][1] - 1]
				else:
					self.pstring = self.pstring + self.player[i][0] + self.cardFace[self.player[i][1] - 1] + ', '
		elif turn == 'dealer':
			self.dtotal = self.checkValue('dealer')
			self.dstring = ''
			for i in range(len(self.dealer)):
				if i == len(self.dealer) - 1:
					if i == 0 and self.gameState == 1:
						self.dstring = self.dstring + ':grey_question:'
					else:
						self.dstring = self.dstring + self.dealer[i][0] + self.cardFace[self.dealer[i][1] - 1]
				else:
					if i == 0 and self.gameState == 1:
						self.dstring = self.dstring + ':grey_question:, '
					else:
						self.dstring = self.dstring + self.dealer[i][0] + self.cardFace[self.dealer[i][1] - 1] + ', '
		self.board = f"{self.user}'s' Total: {self.ptotal}\nCards: [{self.pstring}]\n \nDealer's Total: {self.dtotal}\nCards: [{self.dstring}]"

	def hit(self):
		print('hit')
		if self.pstand == 0:
			deal = random.choice(self.cards)
			self.cards.remove(deal)
			self.player.append(deal)
			self.updateBoard('player')
			if self.ptotal > 21:
				self.status = f"{self.user.upper()} BUSTED!"
				self.gameState = 0
		elif self.dstand == 1:
			checkWinner()
		else:
			return

	def stand(self):
		print('stand')
		self.pstand = 1

	def deal(self):
		print('deal')
		if self.dstand == 0:
			deal = random.choice(self.cards)
			self.cards.remove(deal)
			self.dealer.append(deal)
			self.updateBoard('dealer')
			if self.dtotal > 21:
				self.status = f"THE DEALER BUSTED. {self.user.upper()} WINS!"
				self.gameState = 0
			elif self.dtotal > 16:
				self.dstand = 1
		elif self.pstand == 1:
			self.checkWinner()
		else:
			return

	def checkValue(self,turn):
		print('check')
		if turn == 'player':
			hand = self.player
		else:
			hand = self.dealer
		aces = 0
		total = 0
		for i in range(len(hand)):
			cardValue = hand[i][1]
			if cardValue == 1:
				aces = aces + 1
			elif cardValue > 9:
				total = total + 10
			else:
				total = total + cardValue
		if aces > 0:
			eleven = 11 + total + (aces-1)
			if eleven > 21:
				total = total + aces
			else:
				total = eleven
		return total


	def checkWinner(self):
		self.ptotal = self.checkValue('player')
		self.dtotal = self.checkValue('dealer')
		if self.ptotal > self.dtotal:
			self.status = f"{self.user}'s total is {self.ptotal}. The dealer's total is {self.dtotal}. {self.user.upper()} WINS!"
		elif self.ptotal == self.dtotal:
			self.status = f"{self.user}'s total is {self.ptotal}. The dealer's total is {self.dtotal}. IT'S A TIE."
		else:
			self.status = f"{self.user}'s total is {self.ptotal}. The dealer's total is {self.dtotal}. {self.user.upper()} LOSES!"
		self.gameState = 0



class Blackjack(commands.Cog):

	def __init__(self,bot):
		self.bot = bot
		self.users = {}

	@commands.command()
	async def blackjack(self,ctx,money=0):
		self.users[ctx.message.author] = BJGame(ctx.message.author)
		game = self.users[ctx.message.author]
		embed = discord.Embed(
			title = "Blackjack",
			colour = discord.Colour.from_rgb(178, 107, 209)
			)
		embed.add_field(name = game.status, value = game.board , inline = False)
		await ctx.send(embed=embed)


	@commands.Cog.listener()
	async def on_message(self,message):
		if message.content == "hit" and message.author in self.users:
			if self.users[message.author].gameState == 1:
				game = self.users[message.author]
				game.hit()
				game.deal()
				embed = discord.Embed(
					title = "Blackjack",
					colour = discord.Colour.from_rgb(178, 107, 209)
					)
				game.updateBoard('dealer')
				embed.add_field(name = game.status, value = game.board , inline = False)
				await message.channel.send(embed=embed)
		elif message.content == "stand" and message.author in self.users:
			if self.users[message.author].gameState == 1:
				game = self.users[message.author]
				game.stand()
				for i in range(21):
					if game.gameState == 1:
						game.deal()
					else:
						continue
				embed = discord.Embed(
					title = "Blackjack",
					colour = discord.Colour.from_rgb(178, 107, 209)
					)
				game.updateBoard('dealer')
				embed.add_field(name = game.status, value = game.board , inline = False)
				await message.channel.send(embed=embed)




def setup(sushi):
	sushi.add_cog(Blackjack(sushi))