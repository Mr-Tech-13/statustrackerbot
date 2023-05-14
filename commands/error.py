from discord.ext import commands
import asyncio

class clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def error(ctx, title, description):
        channel = ctx.channel
        await channel.edit(name='\N{LARGE YELLOW CIRCLE} Service-Status')
        await ctx.channel.purge()
        embed = discord.Embed(title='Service Status', description=':orange_circle: Online with errors, see below', color=0xFFFF00)
        embed.set_author(name='*This embed updates when the service status changes*')
        message = await ctx.send(embed=embed)
        embed = discord.Embed(title=':yellow_circle: Caution', description=message, color=0xFFFF00)
        await ctx.send(embed=embed)
        embed = discord.Embed(title=title, description=description, color=0xFFFF00)
        message = await ctx.send(embed=embed)
        global embed_message_id
        embed_message_id = message.id
        with open('message_id.txt', 'w') as f:
          f.write(str(embed_message_id))

def setup(client):
    client.add_cog(clear(client))
    