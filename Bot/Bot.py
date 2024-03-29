# Invite: https://discordapp.com/api/oauth2/authorize?client_id=591950692214636594&permissions=8&scope=bot

import json
import aiml
from DavesLogger import Logs

import discord
from discord.ext import commands

class Chatto (commands.Bot):
    def __init__ (self):
        super ().__init__ (
            command_prefix = self.Prefix,
            description = self.Description,
            activity = discord.Game (name = self.Status.format (self.Prefix)),
            case_insensitive = True,
            max_messages = 10_000
        )

        self.Kernel = aiml.Kernel ()
        self.Setup ()

    @property
    def Config (self) -> dict:
        with open ('Config.json', 'r') as Config:
            return json.loads (Config.read ())

    @property
    def Prefix (self) -> str:
        return self.Config.get ('Prefix', '--')

    @property
    def Description (self) -> str:
        return self.Config.get ('Description', 'Hello! I\'m Chatto, a fun chat bot for your Discord server!')

    @property
    def Status (self) -> str:
        return self.Config.get ('Status', 'Help: {}help')

    def Setup (self):
        self.Kernel.learn ('Data/Startup.xml')
        self.Kernel.respond ('LOAD AIML B')

    def LoadExtensions (self, _Path: str = '', _Extensions: list = [], _Suffix: str = '') -> None:
        for Extension in _Extensions:
            Name = Extension.split ('.')[-1]
            Extension = f'{_Path}.{Extension}{_Suffix}'

            try:
                self.load_extension (Extension)

            except Exception as Error:
                ErrorMessage = f'{Name} cannot be loaded. Error: {Error}'
                Logs.Error (ErrorMessage)

    def Run (self) -> None:
        self.remove_command ('help')

        self.LoadExtensions ('Commands', self.Config.get ('Commands', []), 'Command')
        self.LoadExtensions ('Modules', self.Config.get ('Modules', []))

        self.run (self.Config.get ('Token', ''))
