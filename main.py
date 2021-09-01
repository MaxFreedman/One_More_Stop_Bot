# Dependency Setup ------------------------------
import discord
from discord.ext import commands
import os
from webserver import keep_alive
from dotenv import load_dotenv

# Client initilization and define prefix -------------------------------------
intents = discord.Intents.default()
intents.members = True
load_dotenv()
bot = commands.Bot(command_prefix='--',
                   help_command=None,
                   intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name='these TONEZ'))
    print(f'{bot.user} has connected to Discord!')
    print('----------------------------------------')


# Error handling -------------------------------------------------------------
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"I'm sorry {ctx.author.mention}, I'm afraid I can't"
                       " let you do that.", delete_after=5.0)
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention}, it seems you're forgetting"
                       " something.", delete_after=5.0)
        await ctx.message.delete()


# Run the client on the server -----------------------------------------------
cogs_folder_path = './/cogs'

for file in os.listdir(cogs_folder_path):
    if file.endswith(".py") and not file.startswith("_"):
        bot.load_extension(f'cogs.{file[:-3]}')

    else:
        print(f'Unable to load {file[:-3]}')

keep_alive()
token = os.environ['token']
bot.run(token)
