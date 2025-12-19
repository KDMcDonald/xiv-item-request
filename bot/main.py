# Standard Libraries
import logging

# 3rd Party Libraries
import keyring
import nextcord
from nextcord.ext import commands

# Custom Libraries
from utils import args

def setup():
    # Get arguments from command line
    arguments = args.get_args()

    # Setup logging for nextcord
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.getLevelName(arguments.logginglevel))
    handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    # Setup the bot
    bot = commands.Bot(intents=nextcord.Intents.default())
    testing_guild = arguments.testingguild
    token = keyring.get_password(service_name=arguments.tokenservice, username=arguments.tokenname)

    if token == None:
        print(f'No token found! Cannot run bot.')
        exit()

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')
    

    bot.run(token)
