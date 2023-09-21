# hello World
import asyncio
import discord
from discord.ext import commands

# Read the token and channel ID from the file
with open('token.txt') as f:
    token = f.readline().strip()
    channel_id = int(f.readline().strip())

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
embed_message_id = None # define the variable to store the message ID

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
async def offline(ctx):
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

@client.command()
async def warning(ctx, *, messagea):
    await ctx.channel.purge()
    channel = ctx.channel
    await channel.edit(name='\N{LARGE ORANGE CIRCLE} Service-Status')
    await ctx.channel.purge()
    embed = discord.Embed(title='Service Status', description=':orange_circle: Service Unstable, see below', color=0xffa500)
    embed.set_author(name='*This embed updates when the service status changes*')
    message = await ctx.send(embed=embed)
    embed = discord.Embed(title=':orange_circle: Warning!', description=messagea, color=0xffa500)
    await ctx.send(embed=embed)

@client.command()
async def error(ctx, title, description):
    channel = ctx.channel
    await channel.edit(name='\N{LARGE YELLOW CIRCLE} Service-Status')
    await ctx.channel.purge()
    embeda = discord.Embed(title='Service Status', description=':orange_circle: Online with errors, see below', color=0xFFFF00)
    embeda.set_author(name='*This embed updates when the service status changes*')
    message = await ctx.send(embed=embeda)
    embed = discord.Embed(title=':yellow_circle: Caution', description=messagea, color=0xFFFF00)
    await ctx.send(embed=embed)
    embedb = discord.Embed(title=title, description=description, color=0xFFFF00)
    messagea = await ctx.send(embed=embedb)
    global embed_message_id
    embed_message_id = message.id
    with open('message_id.txt', 'w') as f:
        f.write(str(embed_message_id))

@client.command()
async def online(ctx):
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

@client.command()
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

@client.command()
async def shutdown(ctx):
    await ctx.send('Shutting down...')
    await ctx.channel.purge()
    await client.close()

@client.command()
async def stop(ctx):
    await ctx.send('Stopping...')
    await client.close()

@client.command()
async def commands(ctx):
    await ctx.message.delete()
    with open('commands.txt', 'r') as f:
        commands_text = f.read()
    embed = discord.Embed(title='Bot Commands', description=commands_text, color=0x00ff00)
    message = await ctx.send(embed=embed)
    global embed_message_id
    embed_message_id = message.id
    with open('message_id.txt', 'w') as f:
        f.write(str(embed_message_id))
    await asyncio.sleep(10)
    await message.delete()


@client.command()
async def colors(ctx):
    await ctx.channel.purge()
    embed = discord.Embed(title='Color Codes', description='\N{LARGE GREEN CIRCLE}=No issues, Service is online \n\N{LARGE YELLOW CIRCLE}=Error Detected, See below for more info. Service should still be running \n\N{LARGE ORANGE CIRCLE}=Service is unstable, See below for more info. \n\N{LARGE RED CIRCLE}=Service is unavailable, See below for more info.')
    message = await ctx.send(embed=embed)
    global embed_message_id
    embed_message_id = message.id
    with open('message_id.txt', 'w') as f:
        f.write(str(embed_message_id))
    await asyncio.sleep(10)
    await message.delete()

@client.command()
async def stream(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Streams!', description='\n Main streams: \nYoutube: https://www.youtube.com/channel/UCdrIqmWKVA2MKeP_VBNHWMg/live \nTwitch: https://www.twitch.tv/fstimelapses \n Backup Stream: \nhttps://www.youtube.com/watch?v=Giub2JmpXhA')
    message = await ctx.send(embed=embed)
    global embed_message_id
    embed_message_id = message.id
    with open('message_id.txt', 'w') as f:
        f.write(str(embed_message_id))

@client.command()
async def streamup(ctx):
    channel = ctx.channel
    await ctx.message.delete()
    await channel.edit(name='\N{LARGE GREEN CIRCLE} Streams')

@client.command()
async def streamdown(ctx):
    channel = ctx.channel
    await ctx.message.delete()
    await channel.edit(name='\N{LARGE RED CIRCLE} Streams')


# Ban a user from the server
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned.')

# Unban a user from the server
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user} has been unbanned.')
            return

    await ctx.send(f'{member} was not found in the ban list.')

@client.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)
        await member.add_roles(muted_role, reason=reason)
        await ctx.send(f"{member.mention} has been muted.")
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command()
async def unmute(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("There are no muted roles on this server.")
            return
        if muted_role not in member.roles:
            await ctx.send(f"{member.mention} is not muted.")
            return
        await member.remove_roles(muted_role, reason="Unmuted")
        await ctx.send(f"{member.mention} has been unmuted.")
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        embed = discord.Embed(title="User Warned", description=f"{member.mention} has been warned.", color=0xFFFF00)
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command()
async def purge(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        deleted = await ctx.channel.purge(limit=amount+1)
        embed = discord.Embed(description=f"{len(deleted)-1} messages have been purged.", color=0xFF0000)
        await ctx.send(embed=embed, delete_after=5)
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked.", color=0xFF0000)
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have permission to use this command.")



# Run the bot using the token
client.run(token)
