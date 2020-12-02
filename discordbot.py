# exitを使うため
import sys
# discordのAPI
import discord
# Google検索
from googlesearch import search

# 接続に必要らしい(よくわかってない)
client = discord.Client()

# とりあえずフラグでモード管理しようかなと
ModeFlag = 0

# 起動時のメッセージ
@client.event
async def on_ready():
    # 起動時にメッセージの送信
    channel = client.get_channel(チャンネルID)
    await channel.send('監視してるよ＾＾')

# メッセージを受けた時の動作
@client.event
async def on_message(message):
    # イベント入るたびに初期化はまずいのでグローバル変数で
    global ModeFlag
    # botの発言は無視する(無限ループ回避)
    if message.author.bot:
        return
    # 一応終了するコマンドも用意しておく
    if message.content == '!exit':
        await message.channel.send('ﾉｼ')
        sys.exit()
    # google検索モード(次に何か入力されるとそれを検索)
    if ModeFlag == 1:
        kensaku = message.content
        ModeFlag = 0
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(kensaku, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break
    # google検索モードへの切り替え
    if message.content == '!google':
        ModeFlag = 1
        await message.channel.send('検索するワードをチャットで発言してね')
    # 単純な応答
    if message.content == 'bot君いる？':
        await message.channel.send('私bot君。あなたの後ろにいるよ。')
    # 特定の文字から始まる文章が発言されたとき
    if message.content.startswith('負け'):
        lose = message.author.name + "の負け！ｗ"
        await message.channel.send(lose)
    #リプライを受け取った時
    if client.user in message.mentions:
        reply = f'{message.author.mention} うるさいよ。'
        await message.channel.send(reply)
    # これについては触れないよ。
    if message.content.startswith("なんだかんだ"):
        kanda = "かんだ・・・神田ァ！？\n" + "https://www.youtube.com/watch?v=KUwpssJX37M"
        await message.channel.send(kanda)
# botの起動と接続
client.run('botのアクセストークン')
