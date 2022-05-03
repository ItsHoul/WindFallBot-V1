import nextcord
import http
import json
import os
from nextcord.ext import commands
from nextcord import Interaction


#начало ебни 1 

def get_prefix(client, message):
    with open ('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

#конец ебни 1


intents = nextcord.Intents.default()
intents.members = True

statusus = nextcord.Activity(type = nextcord.ActivityType.watching, name = "https://owodev.ml")
client = commands.Bot(command_prefix=get_prefix, status=nextcord.Status.dnd, activity=statusus, intents=intents)
client.remove_command('help')



#ебня 2

@client.event
async def on_guild_join(guild): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f) 

    prefixes[str(guild.id)] = 'wf!'#default prefix

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f)
    prefixes.pop(str(guild.id)) 
    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True) 
async def changeprefix(ctx, prefix): 
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Changed prefix to: {prefix}') 

#ебня 2


@client.command(aliases=["quit"])
async def posholnahuy(ctx):
    if int(ctx.author.id) == "BOT OWNER ID MOMENT": 
        await client.close()
        print("Client got rekt")
    else:
        await ctx.send("<:tu:957874380032077854>")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("Мам, я слил токен((((")
