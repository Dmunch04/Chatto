from DavesLogger import Logs

import discord
from discord.ext import commands

class Events (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.Cog.listener ()
    async def on_ready (self):
        Logs.Server ('Chatto has been booted ;)')

    @commands.Cog.listener ()
    async def on_message (self, _Message: str):
        Sender = _Message.author
        Channel = _Message.channel
        Message = _Message.content

        if Channel.name == self.Client.Config.get ('ChatChannel', 'chat') and Sender.id != self.Client.user.id:
            async with Channel.typing ():
                Response = self.Client.Kernel.respond (Message)

                if Response:
                    await Channel.send (Response)

def setup (_Client):
    _Client.add_cog (Events (_Client))
