import discord
from splatoon2 import Stage
from gear_setting import gear

TOKEN = ""
time_list = ['01','03','05','07','09','11','13','15','17','19','21','23']
topics = gear

client = discord.Client()

@client.event
async def on_ready():
    print("開始")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content in topics.keys():
        text = message.content
        await reply_topic(message,text)

    if message.content == 'help':
        await message.channel.send(f"コマンド一覧\n{', '.join(topics.keys())}")

    if message.content == '/now':
        stage = Stage()
        li = stage.get_now()
        await reply(message,li)

    if message.content == '/next':
        stage = Stage()
        li = stage.get_next()
        await reply(message,li)

    if message.content[1:3] in time_list:
        stage = Stage()
        li = stage.get_time(message.content[1:3])
        await reply(message,li)

async def reply(message,li):
        await message.channel.send(f"{li[0]}\n{li[1]} -> {li[2]}, {li[3]}\n{li[4]} -> {li[5]}, {li[6]}\n{li[7]} -> {li[8]}, {li[9]}")

async def reply_topic(message,i):
    await message.channel.send(f"付きやすい -> {topics[i][0][0]}\n付きにくい -> {topics[i][1][0]}\n説明: {topics[i][2][0]}\n補足: {topics[i][3][0]}")

client.run(TOKEN)