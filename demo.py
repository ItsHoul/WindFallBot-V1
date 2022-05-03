import nextcord
import json
from nextcord.ext import commands
from nextcord import Interaction

class Demo(commands.Cog):

    

    def __init__(self, client):    
        self.client = client


    @nextcord.slash_command()
    async def debugone(self, interaction: Interaction):
        await interaction.response.send_message("y u susy baka")



    @commands.command()
    async def knop(self, ctx):
        @nextcord.ui.button(label="ужас", style=nextcord.ButtonStyle.green)
        async def knopb(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            await interaction.response.send_message('да ужас', ephemeral=False)


    @commands.Cog.listener()
    async def on_ready(self):
        print("WindFallBot : ready")
        startedchannel = self.client.get_channel(903953765051297812)
        await startedchannel.send("✅ Bot has started")
        for guild in self.client.guilds:
            print(guild.name)



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        sayhiemb = nextcord.Embed(title = "Hey :D", description = "Thanks for inviting me to your server!")
        sayhiemb.add_field(name = "Remember :", value="This bot can be unstable sometimes, because it's being hosted on a crappy laptop :D")
        if guild.system_channel:
            await guild.system_channel.send(embed=sayhiemb)

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("Cogs are working fine, there are **3 COGS**")


    @commands.command()
    async def chat(self, ctx, channel, *msg):
        if int(ctx.author.id) == 596637934216806410: 
            bebrakanal = self.client.get_channel(int(channel))
            msgcont = " ".join(msg)
            await bebrakanal.send(msgcont)
        else:
            print("Уньки дуньки пуньки пу!")



    @commands.Cog.listener()
    async def on_message(self, message:str):
        logchannel = self.client.get_channel(903953765051297812)
        print(f'{message.author} : {message.content} / Channel : #{message.channel} / ChannelID : {message.channel.id} / Server :{message.guild}')

    '''@commands.command()
    async def play(self, ctx):
        trollembed1 = nextcord.Embed(title = f'Play command', description = "Uh oh! This feature is only avalible to WindFallBot premium subscribers!", color=0x2D4FE4)
        trollembed1.add_field(name = "Subscribe to WindFallBot premium here :", value = "https://poshelnah.ui/pidoras.js")
        trollembed1.set_thumbnail(url="https://cdn.discordapp.com/emojis/888864448272556042.webp?size=56&quality=lossless")
        await ctx.send(embed = trollembed1)'''


def setup(client):
    client.add_cog(Demo(client))
