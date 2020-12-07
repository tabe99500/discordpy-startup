from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(neme='ひよこ')
async def ひよこ(ctx):
    await ctx.send('ぴよよ～')

@bot.command(name='疲れた')
async def 疲れた(ctx):
    await ctx.send('ぴよ？？？？？')
    
@bot.command(name='よりくん')
async def よりくん(ctx):
    await ctx.send('ぴよっ💓')

@bot.command(name=['DISCORD_BOT_ID'])
async def name(ctx):
    await ctx.channel.send('きゃすへの殺意が高まる～')
    
bot.run(token)
