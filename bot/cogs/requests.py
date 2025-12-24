# 3rd Party Libraries
import nextcord
from nextcord.ext import commands

# Custom Libraries
from bot import XIVRequestBot
from utils.config import guild_id


class Requests(commands.Cog):
    def __init__(self, bot : XIVRequestBot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.info(f'{self.__class__.__name__} has loaded successfully.')

    @nextcord.slash_command(
        name='hello_world',
        description='A test command for testing features.',
        guild_ids=guild_id
    )
    async def hello_world(self, interaction : nextcord.Interaction):
        await interaction.response.send_message("This is a test!")

def setup(bot : XIVRequestBot):
    bot.add_cog(Requests(bot=bot))

