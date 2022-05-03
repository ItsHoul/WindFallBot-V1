import nextcord
import requests
import json
import wget
import urllib.request
from nextcord.ext import commands
from PIL import Image
from owoify import *

class Fun(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.command()
    async def meme(self, ctx):
        lecont = requests.get("https://meme-api.herokuapp.com/gimme").text
        datik = json.loads(lecont,)
        sendamem = nextcord.Embed(title=f"{datik['title']}", color=nextcord.Color.random())
        sendamem.set_image(url=f"{datik['url']}")
        await ctx.reply(embed=sendamem)

 


    @commands.command()
    async def fox(self, ctx):
        foxxo = requests.get("https://some-random-api.ml/animal/fox").text
        ledata = json.loads(foxxo,)
        sendafox = nextcord.Embed(title="🦊", color = 0xFFD848)
        sendafox.set_image(url=f"{ledata['image']}")
        await ctx.reply(embed=sendafox)

    @commands.command(aliases=["owoify"])
    async def owo(self, ctx, *texto:str):
        someargs = " ".join(texto)
        await ctx.send(owoify(f"{someargs}"))

    @commands.command(aliases=["owounreadable"])
    async def owoinsane(self, ctx, texto:str):
        await ctx.send(owoify(f"{texto}", 'uvu'))


    @commands.command()
    async def screenshot(self, ctx, site = "https://google.com"):
        await ctx.send(f"https://api.popcat.xyz/screenshot?url={site}")


    #блять ебучий scratch API
    @commands.command()
    async def scratchuser(self, ctx, username:str):
        scratchuser = requests.get(f"https://api.scratch.mit.edu/users/{username}").text
        datascr = json.loads(scratchuser,)
        suseremb = nextcord.Embed(title=f"Information about {username}", color=0xFFD848)
        suseremb.add_field(name="Username", value=f"{datascr['username']}")
        suseremb.add_field(name="ID", value=f"{datascr['id']}")
        suseremb.add_field(name="Country", value=f"{datascr['profile']['country']}")
        suseremb.add_field(name="Status", value=f"{datascr['profile']['status']}")
        suseremb.add_field(name="About me", value=f"{datascr['profile']['bio']}")
        suseremb.set_author(name=f"{username}", icon_url=f"{datascr['profile']['images']['90x90']}")
        suseremb.set_thumbnail(url=f"{datascr['profile']['images']['90x90']}")
        await ctx.reply(embed=suseremb)


    @commands.command(aliases=["wfav"])
    async def wfavatar(self, ctx, member: nextcord.Member = None):
        if not member:
            member = ctx.message.author
        lepfp = str(member.avatar)
        opener = urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        filename = 'userpfp.png'
        image_url = lepfp
        urllib.request.urlretrieve(image_url, filename)

        foredit = Image.open(r"userpfp.png")
        foredit = foredit.resize((500, 500))
        lemask = Image.open(r"oblozh.png")
        lemask = lemask.resize((500, 500))

        navihod = Image.alpha_composite(foredit, lemask)
        navihod.save('navihod.png')
        finalemb = nextcord.Embed(title="WFBot'd avatar", color=0xFFD848)
        finalefl = nextcord.File("navihod.png", filename="wfbotav.png")
        finalemb.set_image(url="attachment://wfbotav.png")
        await ctx.send(file=finalefl, embed=finalemb)

    @commands.command(aliases=["bbl", "messagebox", "speechbubble"])
    async def bubble(self, ctx, member: nextcord.Member = None):
        if not member:
            member = ctx.message.author
        lepfp = str(member.avatar)
        opener = urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        filename = 'userpfp.png'
        image_url = lepfp
        urllib.request.urlretrieve(image_url, filename)

        foredite = Image.open(r"userpfp.png")
        foredite = foredite.resize((500, 500))
        lemaske = Image.open(r"messageboxlmao.png")
        lemaske = lemaske.resize((500, 500))

        navihod = Image.alpha_composite(foredite, lemaske)
        navihod.save('navihod.png')
        finalemb = nextcord.Embed(title="Speech bubble", color=0xFFD848)
        finalefl = nextcord.File("navihod.png", filename="wfbotav.png")
        finalemb.set_image(url="attachment://wfbotav.png")
        await ctx.send(file=finalefl, embed=finalemb)

        print("SUCCESS")


    @commands.command()
    async def dbdb(self, ctx):
        opener = urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        filename = 'userpfp.png'
        image_url = "https://cdn.discordapp.com/avatars/887976025273806870/595d318f6cf15868d98183ddca7d52f9.png"
        urllib.request.urlretrieve(image_url, filename)
        print("ok")





def setup(client):
    client.add_cog(Fun(client))
