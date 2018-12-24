import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="You | Do .help", type=3))
    print ("Bot is ready!")

@client.event
async def on_message(message):
    if "You just said Yhac!" not in message.content:
        if "YHAC" in message.content.upper():
                await client.send_message(message.channel, "You just said Yhac!")
                
    num = random.randint(1,6)
    if message.content.upper().startswith(".ROLL"):
        userID = message.author.id
        #await client.send_message(message.channel, "<@{}>".format(userID)) <--- Tags the user
        await client.send_message(message.channel, "`Your number is: " + str(num) + "`")

    if message.content.upper().startswith(".HELP"):
        await client.send_message(message.channel, "```.roll - Rolls a dice. \n.embed - Repeats the message sent by the user in an embeded box. (Staff Only) \n.say - Repeats the message sent by the user.```")

    if message.content.upper().startswith(".SAY"):
        if " " in message.content:
            if "LEL" in message.content.upper()[5:8]:
                await client.send_message(client.get_channel("526097305439567892"), message.content[9:])
            elif "GENERAL" in message.content.upper()[5:12]:
                await client.send_message(client.get_channel("525065826194161707"), message.content[13:])
            else:
                await client.send_message(message.channel, "`Correct Usage: .say (Channel Name) (Message)`")
        else:
            await client.send_message(message.channel, "`Correct Usage: .say (Channel Name) (Message)`")

    embed = discord.Embed(
        title = "**Message:**",
        description = message.content[7:],
        colour = discord.Colour.green())
    
    if message.content.upper().startswith(".EMBED"):
        if "526035746352660492" in [role.id for role in message.author.roles]:
            if " " in message.content:
                message.content.split() 
                AuthorName = message.author.name
                args = message.content.split(" ")
                pfp = message.author.avatar_url
                embed.set_author(name = AuthorName, icon_url= pfp)
                await client.send_message(client.get_channel("526100768307150850"), embed = embed)
            else:
                await client.send_message(message.channel, "`Correct Usage: .embed (Message)`")
        else:
            await client.send_message(message.channel, "You must be Staff to do this!")


        
                  
##@client.event
##async def on_message(message):
##    embed = discord.Embed(
##        title = "**Message:**",
##        description = message.content[7:],
##        colour = discord.Colour.blue())
##    
##    if message.content.upper().startswith(".EMBED"):
##        if " " in message.content:
##            message.content.split() 
##            AuthorName = message.author.name
##            args = message.content.split(" ")
##            pfp = message.author.avatar_url
##            embed.set_author(name = AuthorName, icon_url= pfp)
##            await client.send_message(message.channel, embed = embed)
##        else:
##            await client.send_message(message.channel, "`Correct Usage: .embed (Message)`")
    
client.run("NTI2MDI1NDQ0ODA2NDkyMTcy.Dv_LIw.nhZf-hM3EG82XrddBm_ITp3suFE")
