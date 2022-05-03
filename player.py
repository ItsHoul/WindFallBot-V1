import nextcord
from nextcord.ext import commands

class Player(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.command()
    async def joinvc(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command()
    async def playsound(self, ctx):
        try:
            servervoice = ctx.message.guild
            vcchannel = servervoice.voice_client

            await ctx.send("bew")

        except:
            await ctx.send("ne bebra")


    @commands.command()
    async def blyat(self, ctx):
        if ctx.message.author.voice:
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
            servik = ctx.guild
            levoice: nextcord.VoiceClient = nextcord.utils.get(self.client.voice_clients, guild=servik)
            surs = nextcord.FFmpegPCMAudio('blyaat.mp3')
            if not levoice.is_playing():
                levoice.play(surs, after = None)


    @commands.command()
    async def playlocal(self, ctx, wef:str):
        if ctx.message.author.voice:
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
            servik = ctx.guild
            levoice: nextcord.VoiceClient = nextcord.utils.get(self.client.voice_clients, guild=servik)
            surs = nextcord.FFmpegPCMAudio(wef)
            if not levoice.is_playing():
                await ctx.send(f"🎵 Trying to play a local file")
                levoice.play(surs, after = None)

    @commands.command()
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("lol")



def setup(client):
    client.add_cog(Player(client))