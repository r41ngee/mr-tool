import disnake
import dotenv
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.InteractionBot(
    intents=intents,
    test_guilds=[1201541446340186133],
    reload=True,
    status=disnake.Status.dnd,
)

cogs = [
    "cogs.misc",
]

for i in cogs:
    bot.load_extension(i)

bot.run(token=dotenv.get_key(".env", "token"))