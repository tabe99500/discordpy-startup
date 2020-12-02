from discord.ext import commands
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行


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
    
bot.run(token)
