import discord

from discord.ext import commands
from random import randint

from config import TOKEN, PREFIX

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIX),
    help_command=None
)

@bot.event
async def on_ready():
    print(f'Log in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send('hi!')


@bot.command()
async def roll(ctx, limit: int=100):
    """
    invoke by !roll    # roll with default limit value ( 100 )
    
    or by !roll 1337   # with changed limit up to 1337
    """
    
    random_value = randint(0, limit)
    
    await ctx.send(f'**{random_value}**')


bot.run(TOKEN)
