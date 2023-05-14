from discord.ext import commands

class Warning(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def warning(self, ctx, *, messagea):
        await ctx.channel.purge()
        channel = ctx.channel
        await channel.edit(name='\N{LARGE ORANGE CIRCLE} Service-Status')
        await ctx.channel.purge()
        embed = discord.Embed(title='Service Status', description=':orange_circle: Service Unstable, see below', color=0xffa500)
        embed.set_author(name='*This embed updates when the service status changes*')
        message = await ctx.send(embed=embed)
        embed = discord.Embed(title=':orange_circle: Warning!', description=messagea, color=0xffa500)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Warning(client))
