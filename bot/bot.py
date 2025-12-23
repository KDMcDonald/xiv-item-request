# Standard Libraries
import logging

# 3rd Party Libraries
import nextcord
from nextcord.ext import commands

# Custom Libraries
from utils import args, config


INTENTS = nextcord.Intents.default()

arguments = args.get_args()

token = config.get_token(service_name=arguments.tokenservice, username=arguments.tokenname)
if token == None:
    exit()
token = str(token)

class XIVRequestBot(commands.Bot):
    def __init__(self, test_servers : list, config_token : str):
        self.test_servers = test_servers,
        self.config_token = config_token
        super().__init__(
            intents=INTENTS,
            help_command=None
        )

    async def setup_hook(self):
        #TODO: Load Cogs
        pass

    async def on_ready(self):
        await self.change_presence(activity=nextcord.Game(name="Slaying giraffes!"))


bot = XIVRequestBot(test_servers=[arguments.testguild], config_token=token)
bot.run(token)
