import discord
import os
import json
import random

from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

#os.chdir(r'C:\Users\PC\Desktop\PyBot\botData')

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot

client.remove_command('help')

def load_plugins():
    for p in os.listdir("plugins"):
        if p.endswith(".py"):
            p = p.rstrip(".py")
            try:
                bot.load_extension(f'plugins.{p}')
                plugins.append(p)
            except Exception as error:
                exc = "{0}: {1}".format(type(error).__name__, error)
                log.warning(f"Failed to load plugin {p}:\n    {exc}")

@client.event
async def on_ready():
	print("bot now ready...")
	
	await client.change_presence(game=discord.Game(name="PyBot | !help"))

#@client.event
#async def on_member_join(member):
	#with open('users.json', 'r') as f:
		#users = json.load(f)
		
	#await update_data(users, member)
	
	#with open('users.json', 'w') as f:
		#json.dump(users, f)
	
@client.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	
	embed.set_author(name="A list of PyBot Commands")
	embed.add_field(name='!help', value='Shows this list.', inline=False)
	embed.add_field(name='!ping', value='Returns "Pong"', inline=False)
	embed.add_field(name='!say <message>', value='Make the bot say something', inline=False)
	embed.add_field(name='!rolldice', value='Roll a Dice', inline=False)
	embed.add_field(name='!flipcoin', value='Flip a Coin', inline=False)
	
	await client.send_message(ctx.message.author, embed=embed)
	
@client.command(pass_context=True)
async def ping(ctx):
	msg = ctx.message
	userId = msg.author
	await client.send_message(msg.channel, "@%s Pong!" % (userId))
	
@client.command(pass_context=True)
async def say(ctx):
	msg = ctx.message
	cmd = msg.content[5:]
	if cmd != None and cmd != "" and cmd != " ":
		print(cmd)
		args = cmd.split(" ")
		await client.send_message(msg.channel, "%s" % (" ".join(args[0:])))
	
	if msg.content.upper().startswith('!RECORDS'):
		cmd = msg.content[9:]
		args = cmd.split(" ")
		
		if len(msg.mentions) == 1:
			print(args[0])
			print(msg.mentions[0].mention)
			if msg.mentions[0].mention ==  args[0]:
				print("Syntax Correct")
				await client.send_message(msg.channel, "Waiting on Records from %s" % (msg.mentions[0].mention))

@client.command(pass_context=True)
async def rolldice(ctx):
	msg = ctx.message
	await client.send_message(msg.channel, "%s, you rolled a **%s**!" % (msg.author.mention,random.randint(1,6)))	

@client.command(pass_context=True)
async def flipcoin(ctx):
	msg = ctx.message
	side = "Heads"
	if random.randint(1,2) == 1:
		side = "Heads"
	else:
		side = "Tails"
	await client.send_message(msg.channel, "%s, The coin landed on **%s**!" % (msg.author.mention,side))
	
@client.command(pass_context=True)
async def truth(ctx):
	msg = ctx.message
	answers = [
		"No",
		"Nope",
		"No Way",
		"Yes",
		"100%",
		"Definitely",
		"Of Course",
		"Im not sure",
		"What are you talking about"
	]
	answer = answers[random.randint(0,len(answers))]
	await client.send_message(msg.channel, "%s, %s" % (msg.author.mention, answer))

client.run("NDkyOTgxMzYzNTMyNjI3OTgz.DoeUoA.Rn4va2FkKhUqlog_H-b-CzRMy14")
