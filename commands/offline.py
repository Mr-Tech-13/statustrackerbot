from discord.ext import commands

class Offline(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def offline(self, ctx):
        await ctx.channel.purge()
        channel = ctx.channel
        await channel.edit(name='\N{LARGE RED CIRCLE} Service-Status')
        embed = discord.Embed(title='Service Status', description=':red_circle: Service Offline',color=0xff0000)
        embed.set_author(name='*This embed updates when the service status changes*')
        message = await ctx.send(embed=embed)
        global embed_message_id
        embed_message_id = message.id
        with open('message_id.txt', 'w') as f:
            f.write(str(embed_message_id))

def setup(client):
    client.add_cog(Offline(client))
