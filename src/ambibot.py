from discord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

# @bot.command(name='fire')
# async def on_campfire(message):
#     if message.author == bot.user:
#         return
#     channel = message.channel
#     response = 'Gotcha, <@{}>! Playing campfire!'.format(message.author.id)
#     await channel.send(response)

# @bot.command(name='rain')
# async def on_rain(message):
#     if message.author == bot.user:
#         return
#     channel = message.channel
#     response = 'Gotcha, <@{}>! Playing rain!'.format(message.author.id)
#     await channel.send(response)

@bot.command(name='ambi')
async def on_ambi(message):
    if message.author == bot.user:
        return
    channel = message.channel
    # msg = message.text.lower()
    if "rain" in message.message.content.lower():
        response = 'Gotcha, <@{}>! Playing rain!'.format(message.author.id)
        await channel.send(response)
    elif "fire" in message.message.content.lower():
        response = 'Gotcha, <@{}>! Playing campfire!'.format(message.author.id)
        await channel.send(response)
    else:
        response = 'Can I help you, <@{}>?'.format(message.author.id)
        await channel.send(response)


bot.run('PUT YOUR TOKEN HERE!!!!')