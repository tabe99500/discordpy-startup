from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command(neme='ひよこ')
async def ひよこ(ctx):
    await ctx.send('ぴよよ～')

@bot.command(name='疲れた')
async def 疲れた(ctx):
    await ctx.send('ぴよ？？？？？')
    
@bot.command(name='よりくん')
async def よりくん(ctx):
    await ctx.send('ぴよっ💓')

@bot.command(name=os.environ['DISCORD_BOT_ID'])
async def name(ctx):
    await ctx.channel.send('ぴよよ🐥')
    
@bot.command(name=os.environ['DISCORD_BOT_ID_PHONE'])
async def name(ctx):
    await ctx.channel.send('ぴよよ🐥')
    
bot.run(token)
