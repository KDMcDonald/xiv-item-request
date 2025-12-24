# Standard Libraries
import os
import logging

# 3rd Party Libraries
import nextcord
from nextcord.ext import commands

# Custom Libraries
from utils import args, config, log


class XIVRequestBot(commands.Bot):
    def __init__(self, config_token : str, logger : logging.Logger, intents : nextcord.Intents = nextcord.Intents.default()):
        self.config_token = config_token
        self.logger = logger
        super().__init__(
            intents=intents
        )

    async def on_ready(self):
        self.logger.info(f'XIV Item Request Bot has started!')
        
        # Change presence of bot
        await self.change_presence(activity=nextcord.Game(name="Slaying giraffes!"))

        # Check and log test guild
        if config.guild_id != None:
            guild = await self.fetch_guild(config.guild_id[0])
            if guild:
                self.logger.info(f'Test guild set: {guild.name}')


def main():
    # Get arguments from commandline
    arguments = args.get_args()

    # Setup logger
    logger = log.setup_logger(name='XIV Item Request Bot', log_destination=arguments.loggingdestination)

    # Get token from keystore
    logger.info('Retrieving token from keystore...')
    token = config.get_token(service_name=arguments.tokenservice, username=arguments.tokenname)
    if token == None:
        logger.error('No token found.')
        exit()
    token = str(token)

    # Declare intents (if changed)
    intents = nextcord.Intents.default()

    # Setup bot
    bot = XIVRequestBot(config_token=token, logger=logger)
    
    # Setup test guild (if dev)
    # TODO: Check if environment is development or prod
    logger.info('Setting up test guild...')
    config.assign_guild_id(arguments.testguild)

    # Load cogs
    logger.info('Loading cogs...')
    cogs = []
    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py') and '__init__' not in filename:
            cog_name = f'cogs.{filename[:-3]}'
            cogs.append(cog_name)
    bot.load_extensions(cogs)

    # Run bot
    bot.run(token=token)


if __name__ == '__main__':
    main()
