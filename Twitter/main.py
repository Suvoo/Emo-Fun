from os import read
import tweepy
import time
import emoji
import random

def readkey(txt):
    dic = {}
    with open('key.txt',encoding="utf-8") as file:
        f = file.read()
        lines = f.split('\n')
        for line in lines:
            sp = line.split('=')
            dic[sp[0]] = sp[1]
    # print(dic['API Key'])
    return dic[txt]

def emojy(words):
    words = words[2:]

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


api_key = readkey('API Key')
api_secret_key = readkey('API Key Secret')
access_token = readkey('Access Token')
secret_access_token = readkey('Access Token Secret')

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token,secret_access_token)

api = tweepy.API(auth)



# Some important variables which will be used later
bot_id = int(api.me().id_str)
mention_id = 1

# The actual bot
while True:
    mentions = api.mentions_timeline(since_id=mention_id) # Finding mention tweets
    # Iterating through each mention tweet
    for mention in mentions:
        print("Mention tweet found")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        # Checking if the mention tweet is not a reply, we are not the author, and
        # that the mention tweet contains one of the words in our 'words' list
        # so that we can determine if the tweet might be a question.
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            words = mention.text.split(' ')
            if words[1] == 'emo':
                try:
                    ans = emojy(mention.text.split(' '))
                    ans = ans + "@{}"
                    print("Attempting to reply...")
                    api.create_favorite(mention.id)
                    api.update_status(ans.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully replied :)")
                except Exception as exc:
                    print(exc)
            
    time.sleep(15) # The bot will only check for mentions every 15 seconds, unless you tweak this value



