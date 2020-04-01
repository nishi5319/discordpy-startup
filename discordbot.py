from discord.ext import commands
import os
import traceback

import sys
import random
# さいころの和を計算する用の関数
from func import  diceroll

TOKEN = 'Njk0ODE3MDA0NDAxNDU5Mjcy.XoRJUw.XHvgXVtbpxTNcbH0Sh7fCGTHq30'
def diceroll(cnt, max):
    total = 0
    num_list = []
    for i in range(0, cnt):
        # ランダムに1からサイコロの面数までの和を取得しリストに入れる
        num = random.randint(1, max)
        num_list.append(num)
    # さいころの目の総和を計算しリストに入れる
    total = sum(num_list)
    num_list.append(total)
    return num_list

client = discord.Client()

@client.event
async def on_ready():
    print('--------------')
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    channel = client.get_channel('チャンネルID')
    await channel.send('楽しいTRPGを始めましょう！')



@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!dice"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)

bot.run(token)
