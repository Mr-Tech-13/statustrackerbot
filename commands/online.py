import discord
from discord.ext import commands

class Online(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def online(self, ctx):
        channel = ctx.channel
        await ctx.channel.purge()
        await channel.edit(name='\N{LARGE GREEN CIRCLE} Service-Status')
        embed = discord.Embed(title='Service Status', description=':green_circle: Online', color=0x00ff00)
        embed.set_author(name='*This embed updates when the service status changes*')
        message = await ctx.send(embed=embed)
        global embed_message_id
        embed_message_id = message.id
        with open('message_id.txt', 'w') as f:
            f.write(str(embed_message_id))

def setup(client):
    client.add_cog(Online(client))
