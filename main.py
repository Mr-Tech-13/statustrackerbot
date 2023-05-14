import asyncio
import discord
from discord.ext import commands

# Read the token and channel ID from the file
with open('token.txt') as f:
    token = f.readline().strip()
    channel_id = int(f.readline().strip())

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
embed_message_id = None # define the variable to store the message ID

# Import command files
#Temp: client.load_extension('commands.')
client.load_extension('commands.offline')
client.load_extension('commands.ping')
client.load_extension('commands.warning')
client.load_extension('commands.online')
client.load_extension('commands.error')
client.load_extension('commands.clear')

@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    await channel.purge()
    await channel.edit(name='\N{LARGE RED CIRCLE} Service-Status')
    embed = discord.Embed(title='Service Status', description=':red_circle: Service Offline',color=0xff0000)
    embed.set_author(name='*This embed updates when the service status changes*')
    message = await channel.send(embed=embed)
    global embed_message_id
    embed_message_id = message.id
    with open('message_id.txt', 'w') as f:
        f.write(str(embed_message_id))

    #  
    #  await channel.edit(name='\N{LARGE GREEN CIRCLE} Service-Status')
    #  await channel.purge() # clear the channel on startup
    #  embed = discord.Embed(title='Service Status', description=':green_circle: Online', color=0x00ff00)
    #  embed.set_author(name='*This embed updates when the service status changes*')
    #  message = await channel.send(embed=embed)
    #  global embed_message_id
    #  embed_message_id = message.id
    #   with open('message_id.txt', 'w') as f:
    #      f.write(str(embed_message_id))

    print('Bot is ready')


@client.command()
async def shutdown(ctx):
    await ctx.send('Shutting down...')
    await ctx.channel.purge()
    await client.close()

@client.command()
async def stop(ctx):
    await ctx.send('Stopping...')
    await client.close()

# Run the bot
client.run(token)
