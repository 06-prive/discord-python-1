import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
  print("Bot is online!!!")
  
@bot.command()
async def ping(ctx):
  ctx.reply("Pong!")
  
@bot.command()
async def help(ctx):
  embed = discord.Embed(colour = discord.Colour.red(), title="Help menu")
  embed.add_field(name="!ping", value="Ping command.")
  embed.set_footer(text=f"Requested by {ctx.author.name}")
  await ctx.reply(embed=embed)
  
bot.run(os.environ['TOKEN'])
