from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command(neme='ひよこ')
async def ひよこ(ctx):
    await ctx.send('ぴよよ～')
    
bot.run(token)
