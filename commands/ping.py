from discord.ext import commands
import asyncio

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')
        await asyncio.sleep(10)
        await ctx.delete()


def setup(client):
    client.add_cog(Ping(client))
