import discord
from discord.ext import commands
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from _io import BytesIO
import requests

class Images(commands.Cog):


	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def gordon(self,ctx, *args):
		phrase = ''
		for i in range(len(args)):
			if i == len(args) - 1:
				phrase = phrase + args[i]
			else:
				phrase = phrase + args[i] + ' '
		if 'lamb' in args:
			return
		else:
			image = Image.open("gordon.png")
			edit = ImageDraw.Draw(image)
			# font = ImageFont.truetype(<font-file>, <font-size>)
			# draw.text((x, y),"Sample Text",(r,g,b))
			if len(phrase)>10 and len(phrase)<=15:
				font = ImageFont.truetype("impact.ttf", 60)
				edit.text((30, 600),f"THIS {phrase.upper()} IS FUCKING RAW!!!",(255,255,255),font=font)
			elif len(phrase)>19:
				font = ImageFont.truetype("impact.ttf", 55)
				edit.multiline_text((30, 550),f"THIS {phrase.upper()}\nIS FUCKING RAW!!!",(255,255,255),font=font)
			else:
				font = ImageFont.truetype("impact.ttf", 70)
				edit.text((45, 600),f"THIS {phrase.upper()} IS FUCKING RAW!!!",(255,255,255),font=font)
			filename = 'raw.png'
			image.save(filename)
			await ctx.send(file=discord.File(filename))

	@commands.command()
	async def spongebob(self,ctx, *args):
		phrase = ''
		for i in range(len(args)):
			for j in range(len(args[i])):
				if j%2 == 0:
					phrase = phrase + args[i][j].lower()
				else:
					phrase = phrase + args[i][j].upper()
			phrase = phrase + ' '
		image = Image.open("sponge.jpg")
		edit = ImageDraw.Draw(image)
		font = ImageFont.truetype("impact.ttf", 117)
		edit.text((30, 30),phrase,(0,0,0),font=font)
		font = ImageFont.truetype("impact.ttf", 115)
		edit.text((32, 30),phrase,(255,255,255),font=font)
		filename = 'mock.png'
		image.save(filename)
		await ctx.send(file=discord.File(filename))

	@commands.command()
	async def filter(self,ctx, arg):
		sendfile = 0
		for file in ctx.message.attachments:
			sendfile = 1
			link = requests.get(file.url)
			img = Image.open(BytesIO(link.content))
			#converts rgba images to rgb (alpha is the transparency parameter)
			rgbimg = img.convert('RGB')
			rgbimg.save('image.jpg')

			image = cv2.imread('image.jpg')

			filename = 'filtered.jpg'

			if arg == 'blur':
				blurred = cv2.GaussianBlur(image,(55,55,),0)
				cv2.imwrite(filename,blurred)
				await ctx.message.channel.send(file=discord.File(filename))

			elif arg == 'gray':
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				cv2.imwrite(filename,gray)
				await ctx.message.channel.send(file=discord.File(filename))

			elif arg == 'edge':
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				blurred = cv2.GaussianBlur(gray,(5,5,),0)
				edged = cv2.Canny(blurred,85,85)
				cv2.imwrite(filename,edged)
				await ctx.message.channel.send(file=discord.File(filename))

			elif arg == 'edgebad':
				edged = cv2.Canny(image,85,85)
				cv2.imwrite(filename,edged)
				await ctx.message.channel.send(file=discord.File(filename))

			elif arg == 'reflect':
				flip = cv2.flip(image, 1)
				cv2.imwrite(filename,flip)
				await ctx.message.channel.send(file=discord.File(filename))

			elif arg == 'bright':
				array = np.array([[0.01, 0.54, 0.9],[0.4, 0.01, 0.4],[0.01, 0.2, 0.01]])
				# array is a convolution matrix
				bright = cv2.filter2D(image, -1, array)
				cv2.imwrite(filename,bright)
				await ctx.message.channel.send(file=discord.File(filename))

			elif arg == '70s':
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
				cv2.imwrite(filename,gray)
				await ctx.message.channel.send(file=discord.File(filename))
			
			else:
				await ctx.message.channel.send('Improper Usage\nFilters: **blur, gray, edge, reflect, bright, 70s**\nFilter Usage Example: *&filter edge*')

		if sendfile == 0:
			await ctx.message.channel.send('Improper Usage\nFilters: **blur, gray, edge, reflect, bright, 70s**\nFilter Usage Example: *&filter edge*')


def setup(sushi):
	sushi.add_cog(Images(sushi))