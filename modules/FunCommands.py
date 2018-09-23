
import discord
import os
import random

from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

@client.command(pass_context=True)
async def rolldice(ctx):
	msg = ctx.message
	await client.send_message(msg.channel, "%s, you rolled a **%s**!" % (msg.author.mention,random.randint(1,6)))	
  

