import discord

TOKEN = '' #トークンキー

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '!omakoro':
        await message.channel.send(file=discord.File('omakoro.mp4'))

client.run(TOKEN)