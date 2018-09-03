import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
#AuthorID  I'll set these both when we have working stuff
#UserName
try:
        
        Dscrd = discord.Client()
        bot_prefix = ">"
        Dscrd = commands.Bot(command_prefix = bot_prefix)

        Dscrd.remove_command('help')

        @Dscrd.event
        async def on_ready():
                await Dscrd.change_presence(game=discord.Game(name='Being coded.'))
                
                print("Logged in as")
                print(Dscrd.user.name + " (" + Dscrd.user.id + ")" )
             
        @Dscrd.command(pass_context = True)
        async def setup(ctx)
        async def on_message(message):
                AuthorID = Dscrd.user.id
                UserName = Dscrd.user.name
        
                 

        #@Dscrd.command(pass_context = True)
       #async def setup(ctx):
           # await Dscrd.say("Setting up account. Please wait.")
        
            

        Dscrd.run('Token')

except Exception as e:
        print(e)
