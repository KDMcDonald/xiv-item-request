# 3rd Party Libraries
import nextcord
from nextcord.ext import commands, application_checks

# Custom Libraries
from bot import XIVRequestBot
from utils.config import guild_id


class Admin(commands.Cog):
    def __init__(self, bot : XIVRequestBot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.bot.logger.info(f'{self.__class__.__name__} has loaded successfully.')

    @nextcord.slash_command(
        name='add_item',
        description='Adds an item to the request database',
        guild_ids=guild_id
    )
    @application_checks.is_owner()
    async def add_item(self, interaction : nextcord.Interaction, item_name : str = nextcord.SlashOption(description='Name of the item'), item_availability : bool = nextcord.SlashOption(description='True/False: Should the item be made available for request')) -> None:
        try:
            cursor = self.bot.db_connection.cursor()

            statement = '''
            INSERT INTO items (item_name, availability)
            VALUES (?, ?);
            '''

            data = (item_name, item_availability)

            cursor.execute(statement, data)

            self.bot.db_connection.commit()

            await interaction.response.send_message('Item was successfully added to the database!', ephemeral=True)
        except Exception as e:
            self.bot.logger.warning(f'Database error during item insert: {e}')
            await interaction.response.send_message('Item failed to be added to the database! Please try again...', ephemeral=True)


def setup(bot : XIVRequestBot) -> None:
    bot.add_cog(Admin(bot=bot))
