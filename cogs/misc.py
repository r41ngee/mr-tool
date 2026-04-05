import disnake
from disnake.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Check the bot's latency.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        latency = self.bot.latency * 1000  # Convert to milliseconds
        await inter.response.send_message(f"Pong! Latency: {latency:.2f} ms")

    @commands.slash_command(name="purge", description="Permanently delete messages in a channel.")
    async def purge(
        self,
        inter: disnake.AppCmdInter,
        amount: int = commands.Param(description="Number of messages to delete. Defaults to 10", default=10, min_value=1, max_value=500)
    ):
        await inter.response.defer(ephemeral=True)
        deleted = await inter.channel.purge(limit=amount)
        await inter.edit_original_message(f"Deleted {len(deleted)} messages.", delete_after=60)

def setup(bot):
    bot.add_cog(Misc(bot))