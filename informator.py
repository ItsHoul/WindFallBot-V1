import nextcord
from nextcord.ext import commands
from nextcord.components import *

class Informator(commands.Cog):


    def __init__(self, client):    
        self.client = client


    
    @commands.command(aliases=["about"])
    async def botinfo(self, ctx):
        aboutemb = nextcord.Embed(title="About", description="uwu", color=0xFFD848)
        aboutemb.set_thumbnail(url="https://cdn.discordapp.com/attachments/903953765051297812/960114549594402866/WindFallBotcolor3.png")
        aboutemb.add_field(name="Version :", value="beta 0.11")
        aboutemb.add_field(name="Bot library :", value="Nextcord.py")
        aboutemb.add_field(name="Host", value='"Cool" HP 250 G7 craptop with I5-8265u(wu)', inline=False)
        aboutemb.add_field(name="Connected servers :", value=str(len(self.client.guilds)), inline=False)
        aboutemb.add_field(name="Nextcord version :", value=str(nextcord.__version__), inline=False)
        '''aboutemb.set_image(url="https://cdn.discordapp.com/attachments/903953765051297812/960118017667244032/fixed.png")'''
        await ctx.send(embed=aboutemb)


        '''@commands.command(aliases=["helpme"])
        async def help(self, ctx, category = "main"):
            category = category.lower()'''


    
    @commands.command(aliases=["help"])
    async def helpme(self, ctx):
        helpembed = nextcord.Embed(title="List of all WindFallBot commands :", color=0xFFD848)
        helpembed.set_author(name="WindFallBot help", icon_url="https://cdn.discordapp.com/attachments/903953765051297812/959138304144572606/pyfallbotb.png")
        helpembed.add_field(name="🛠️ Moderation commands", value="`ban`, `kick`", inline=False)
        helpembed.add_field(name="📚 Information commands", value="`whois`, `server`, `about`", inline=False)
        helpembed.add_field(name="🧮 Fun commands", value="`meme`, `fox`, `screenshot`, `scratchuser`, `owoify`, `owoinsane`", inline=False)
        await ctx.send(embed=helpembed)



    #epic serverinfo
    '''@commands.command(aliases=["server"])
    async def serverinfo(self, ctx):
        serverinfoemb = nextcord.Embed(title="Server information", color=0x2D4FE4)
        serverinfoemb.add_field(name="Server name:", value=f"{ctx.guild.name}", inline=False)
        serverinfoemb.add_field(name="Server ID:", value=f"{ctx.guild.id}", inline=True)
        await ctx.send(embed=serverinfoemb)'''


    #epic user info command
    @commands.command(aliases=["user"])
    async def whois(self, ctx, member : nextcord.Member = None):
        if not member:
            member = ctx.message.author
        roleslist = [role for role in member.roles]
        whoisemb = nextcord.Embed(title = f'User information : {member}', color=0xFFD848)

        #footer and thumbnail
        whoisemb.set_thumbnail(url=member.avatar)
        whoisemb.set_footer(text=f'Command used by {ctx.author}')

        #fields
        whoisemb.add_field(name = 'User ID :', value = member.id, inline = False)
        whoisemb.add_field(name = 'Server nickname :', value = member.display_name)
        whoisemb.add_field(name="Account created :", value= member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        whoisemb.add_field(name="Joined server on :", value= member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await ctx.send(embed = whoisemb)

    @commands.command(aliases=["serverinfo"])
    async def server(self, ctx):
        serbed = nextcord.Embed(title=f"{ctx.guild}", color=0xFFD848)
        serbed.add_field(name = "Server ID", value = ctx.guild.id, inline = False)
        serbed.add_field(name = "Server owner", value = f"{ctx.guild.owner} ({ctx.guild.owner_id})", inline = False)
        serbed.add_field(name = "Member count", value = ctx.guild.member_count, inline = False)
        serbed.add_field(name = "Text channels", value = len(ctx.guild.text_channels))
        serbed.add_field(name = "Voice channels", value = len(ctx.guild.voice_channels))
        serbed.add_field(name = "Roles", value = len(ctx.guild.roles))
        serbed.add_field(name = "Verification level", value = ctx.guild.verification_level)
        serbed.set_thumbnail(url = ctx.guild.icon)
        serbed.set_footer(text = f"Command used by {ctx.author}")
        serbed.set_author(name="Server information", icon_url = ctx.guild.icon)
        await ctx.send(embed=serbed)





def setup(client):
    client.add_cog(Informator(client))
