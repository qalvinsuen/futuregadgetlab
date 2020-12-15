import discord
from discord.ext import commands
import random

class Hangman:
	 
	def __init__(self,word):
		self.row1 = "----------------------\n"
		self.row2 = "|               :hook:\n"
		self.row3 = "|\n"
		self.row4 = "|\n"
		self.row5 = "|\n"
		self.row6 = "|\n"
		self.row7 = "|\n"
		self.row8 = "|\\_\n"
		words = word.split()
		self.temp9 = []
		for i in range(len(words)):
			row = "_"
			row = row + (len(words[i]) - 1)*" _"
			self.temp9.append(row)
		self.row9 = ''
		for i in self.temp9:
			self.row9 = self.row9 + i + "  "
		self.row9 = self.row9 + "\n"
		# self.row9 = "\\_ \\_ \\_ \\_ \\_ \\_ \\_\n"
		self.row10 = ''
		self.row11 = ''
		self.words = words
		self.phrase = word
		self.guesses = []
		self.counter = 0
		self.gameState = 1
		self.correctGuess = 0 #0 for reset, 1 for true, 2 for false
		self.guessall = 0

	def board(self):
		if self.guessall == 1:
			self.row10 = "|   **{}**\n".format(self.phrase.upper())
			self.guessall = 0
		else:
			self.row9 = ''
			for i in self.temp9:
				self.row9 = self.row9 + i + "    "
			self.row9 = self.row9 + "\n"

		# prevents discord for using "_" as formatting
		rowNine = ''
		for i in self.row9:
			if i == '_':
				rowNine = rowNine + "\\" + i
			else:
				rowNine = rowNine + i

		return (self.row1 + self.row2 + self.row3 + self.row4 + self.row5 + self.row6 + self.row7 + self.row8 + rowNine + self.row10 + self.row11)

	def guess(self,letter):
		self.correctGuess = 2
		if letter in self.guesses:
			return
		else:
			self.guesses.append(letter)
		for j in range(len(self.words)):
			for i in range(len(self.words[j])):
				if letter == self.words[j][i] and self.temp9[j][2*i] == '_':
					# print(self.row9)
					if i == 0:
						self.temp9[j] = letter + self.temp9[j][2*i+1:]
					else:
						self.temp9[j] = self.temp9[j][:2*i] + letter + self.temp9[j][2*i+1:]
					#updates if correct
					self.correctGuess = 1
		if self.correctGuess == 2:
			self.counter = self.counter + 1
		self.row10 = '**Guessed Letters: ['
		for i in range(len(self.guesses)):
			if i == len(self.guesses) - 1:
				self.row10 = self.row10 + self.guesses[i]
			else:
				self.row10 = self.row10 + self.guesses[i] + ', '
		self.row10 = self.row10 + ']**\n'
		return

	def checkWin(self):
		win = True
		for i in range(len(self.words)):
			for letter in self.words[i]:
				if letter not in self.guesses:
					win = False
		if self.guessall == 1:
			win = True
		if win:
			self.row3 = "|\n"
			self.row4 = "|      **:tada: YOU WIN!!!:tada: **  \n"
			self.row5 = "|                                                                      :grinning: \n"
			self.row6 = "|                                                                :muscle::shirt::thumbsup:\n"
			self.row7 = "|                                                                      :jeans: \n"
			self.row8 = "|                                                                    :leg::boot:\n"
			self.row9 = "|   **YOUR WORD WAS:** \n"
			self.row10 = ""
			self.gameState = 0
			self.guesses = []
			self.counter = 0
		return


	def updateWrong(self):
		if self.counter == 1:
			self.row3 = "|               :dizzy_face:\n"
		if self.counter == 2:
			self.row4 = "|               :shirt:\n"
		if self.counter == 3:
			self.row4 = "|        :muscle: :shirt:\n"
		elif self.counter == 4:
			self.row4 = "|        :muscle: :shirt:  :thumbsup:\n"
		elif self.counter == 5:
			self.row5 = "|               :jeans:\n"
		elif self.counter == 6:
			self.row6 = "|             :leg:\n"
		elif self.counter == 7:
			self.row6 = "|             :leg::boot:\n"
		elif self.counter == 8:
			self.row3 = "|\n"
			self.row4 = "|    :skull: **GAME OVER** :skull: \n"
			self.row5 = "|   **YOUR WORD WAS:** \n"
			self.row6 = "|   **{}**\n".format(self.phrase.upper())
			self.row7 = "|\n"
			self.row8 = "|    :shirt::leg::muscle::thumbsup::boot::dizzy_face::jeans:\n"
			self.row10 = ''
			self.gameState = 0
			self.guesses = []
			self.counter = 0
		return



class Hangdler(commands.Cog):

	def __init__(self,bot):
		self.bot = bot
		self.games = {}

	@commands.Cog.listener()
	async def on_message(self,message):
		alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		if message.author == self.bot.user:
		    return
		try:
			if self.games[message.guild].gameState == 1:
				game = self.games[message.guild]
				if message.content.lower() == game.phrase.lower():
					game.guessall = 1
					game.checkWin()
					await message.channel.send(game.board())
				elif len(message.content) == 1:
					if message.content.upper() in alphabet:
						game.guess(message.content.upper())
						if game.correctGuess == 1:
							game.checkWin()
						elif game.correctGuess == 2:
							game.updateWrong()
						await message.channel.send(game.board())
		except:
			return

	@commands.command()
	async def hangman(self,ctx,arg="none"):
		if arg == ('animals'):
			f = open("hangman/animals.txt", "r")
			row11 = "Theme: Animals\n"
		elif arg == ('fruits'):
			f = open("hangman/fruits.txt", "r")
			row11 = "Theme: Fruits\n"
		elif arg == ('restaurant'):
			f = open("hangman/restaurant.txt", "r")
			row11 = "Theme: Restaurant\n"
		elif arg == ('house'):
			f = open("hangman/house.txt", "r")
			row11 = "Theme: House\n"
		elif arg == ('eng'):
			f = open("hangman/math.txt", "r")
			row11 = "Theme: Engineering\n"
		elif arg == ('anime'):
			f = open("hangman/anime.txt", "r")
			row11 = "Theme: Anime\n"
		elif arg == ('pokemon'):
			f = open("hangman/pokemon.txt", "r")
			row11 = "Theme: Pokemon\n"
		elif arg == ('comics'):
			f = open("hangman/comics.txt", "r")
			row11 = "Theme: Comic Book Movies\n"
			
		else:
			dictionaries = ["hangman/animals.txt","hangman/fruits.txt","hangman/restaurant.txt","hangman/house.txt","hangman/pokemon.txt","hangman/comics.txt"]
			themerow = ["Theme: Animals\n","Theme: Fruits\n","Theme: Restaurant\n","Theme: House\n","Theme: Pokemon\n","Theme: Comic Book Movies\n"]
			choice = random.choice(dictionaries)
			f = open(choice, "r")
			row11 = themerow[dictionaries.index(choice)]
		wordlist = f.readlines()
		word = random.choice(wordlist).strip()
		print(word)
		game = Hangman(word.upper())
		self.games[ctx.guild] = game
		game.row11 = row11
			
		await ctx.send(game.board())



def setup(sushi):
	sushi.add_cog(Hangdler(sushi))
