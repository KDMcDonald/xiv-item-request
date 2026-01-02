# 3rd Party Libraries
import nextcord
from nextcord.ext import commands

# Custom Libraries
from bot import XIVRequestBot
from utils.config import guild_id


class Requests(commands.Cog):
    def __init__(self, bot : XIVRequestBot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.bot.logger.info(f'{self.__class__.__name__} has loaded successfully.')


def setup(bot : XIVRequestBot) -> None:
    bot.add_cog(Requests(bot=bot))

