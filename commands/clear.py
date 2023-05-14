from discord.ext import commands
import asyncio

class clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(ctx):
        await ctx.channel.purge()
        print('Cleared channel')
        embed = discord.Embed(description=':green_circle: Cleared!', color=0x00ff00)
        message = await ctx.send(embed=embed)
        global embed_message_id
        embed_message_id = message.id
        with open('message_id.txt', 'w') as f:
             f.write(str(embed_message_id))
        await asyncio.sleep(3)
        await ctx.channel.purge()

def setup(client):
    client.add_cog(clear(client))