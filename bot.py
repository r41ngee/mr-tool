import disnake
import dotenv
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.InteractionBot(
    intents=intents,
    test_guilds=[1434624688830812192, 1201541446340186133, 1483462551818731665],
    reload=True,
    status=disnake.Status.dnd,
)

cogs = [

]

for i in cogs:
    bot.load_extension(i)

bot.run(token=dotenv.get_key(".env", "token"))