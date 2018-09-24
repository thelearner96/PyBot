
import discord
import os
import random

from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Class Funcommands:
	def __init__:
		Pass
	
	@commands.command(name="hi",pass_context=True)
	async def hi(ctx):
		msg = ctx.message
		await client.send_message(msg.channel, "hello")	


  

