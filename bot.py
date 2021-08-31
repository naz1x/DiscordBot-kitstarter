import discord
import config

from discord.ext import commands

bot = commands.Bot(command_prefix = commands.when_mentioned_or(config.prefix), intents = discord.Intents.all(), help_command = None)

@bot.event
async def on_ready():
    print(f'Log in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('hi!')


bot.run(config.token)
