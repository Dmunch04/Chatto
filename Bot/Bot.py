import json

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

    def LoadExtensions (self, _Path: str = '', _Extensions: list = [], _Suffix: str = '') -> None:
        for Extension in _Extensions:
            Name = Extension.split ('.')[-1]
            Extension = f'{_Folder}.{Extension}{_Suffix}'

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
