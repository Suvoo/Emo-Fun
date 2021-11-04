import discord
import emoji
import random

bot = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1

    print("My first bot is in " + guild.name)

def emojy(words):
    words = words[1:]

    options = [ emoji.UNICODE_EMOJI_ENGLISH, emoji.UNICODE_EMOJI_ALIAS_ENGLISH,
            emoji.UNICODE_EMOJI_ITALIAN,emoji.UNICODE_EMOJI_SPANISH,
            emoji.UNICODE_EMOJI_PORTUGUESE  ]

    choi = random.choice(options)
    emo = []
    for i in choi:
        emo.append(i)
    ans = ''
    for w in words:
        # print(w,' ',random.choice(emo))
        ans += w + ' ' + random.choice(emo)
    return ans

@bot.event
async def on_message(message):
    
    if message.content == 'whats':
        await message.channel.send('hey child')
    if message.content == 'master who':
        await message.channel.send('im a slave to @suvoo/AmEnough#6032')

    words = message.content.split(' ')    
    print(words)
    
    if words[0] == 'emo':
        ans = emojy(words)
        # user_message = str(message.content)
        await message.channel.send(ans)
        
    #check if bot onlyresponds to its own message
    

with open('key.txt',encoding="utf-8") as file:
    f = file.read()
    
bot.run(str(f))