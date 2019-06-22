import discord
from discord.ext import commands

class SettingCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (aliases = ['set'])
    @commands.is_owner ()
    async def setting (self, _Type: str, _Sub: str, *, _Value: str) -> None:
        pass

def setup (_Client):
    _Client.add_cog (SettingCommand (_Client))
