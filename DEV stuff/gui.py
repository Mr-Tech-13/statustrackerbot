import wx
import discord
from discord.ext import commands

# Define your Discord bot token
TOKEN = ''
GUILD_ID = ''  # Replace with your server's ID
CHANNEL_ID = ''  # Replace with the channel's ID where you want to send messages


# Set up a bot instance
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Find the target channel
    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)
    bot.channel = channel

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')       
        my_btn = wx.Button(panel, label='Press Me')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            # Send a message to the Discord channel
            message = f'You typed: "{value}"'
            bot.loop.create_task(bot.channel.send(message))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
