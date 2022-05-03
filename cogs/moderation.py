import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):    
        self.client = client
    
    
    #Cute ban command for uwu cute people owo
    @commands.command(aliases=["дать_по_жопе"])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : nextcord.Member = "NONELMAO", *, reason = "No reason provided"):
        if member == "NONELMAO":
            await ctx.send("You should provide a user to ban")
        else:
            amoga = nextcord.Embed(title = f"{member} was banned. Reason : {reason}" , color = 0xFFD848)
            lmaochel = nextcord.Embed(title = f"You've been banned on a random server with reason: {reason}" , color = 0xFFD848)
            await member.ban(reason = reason)
            await member.send(embed = lmaochel)
            await ctx.send(embed = amoga)

    '''@commands.command()
    async def mute(self, ctx, member: nextcord.Member, reasonto = "No reason provided"):
        muterole = nextcord.utils.get(nextcord.Guild.roles, name = "Muted")
        await ctx.add_roles(member, muterole)
        await ctx.send(f"{member} got muted xd for: {reasonto}")'''


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: nextcord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = nextcord.Embed(title=f"{user.name} got kicked :D", description=f"Reason: {reason}\nKicked by: {ctx.author.mention}")
        notify1 = nextcord.Embed(title="You got kicked :D", description=f"With reason: {reason}\nKicked by: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=notify1)




def setup(client):
    client.add_cog(Moderation(client))
