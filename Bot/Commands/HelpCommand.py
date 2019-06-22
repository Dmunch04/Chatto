import discord
from discord.ext import commands

class HelpCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command ()
    async def help (self, ctx):
        ctx.channel.send ('Help is on it\'s way haha')
