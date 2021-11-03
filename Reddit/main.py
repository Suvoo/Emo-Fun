import praw
import emoji
import random
import time

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

client_id = readkey('client id')
client_secret = readkey('client secret')
user_agent = readkey('user agent')
username = readkey('username')
password = readkey('password')

reddit = praw.Reddit(client_id = client_id, 
                     client_secret = client_secret, 
                     user_agent = user_agent,
                     username=username, 
                     password=password
                     ) 

target_sub = "memes"
subreddit = reddit.subreddit(target_sub)
# print(reddit.redditor('suvoo').karma)
for post in subreddit.new(limit=10):
    print('%%%%%%%%%%%%%%%%%%%')
    print(post.title)

for comment in subreddit.stream.comments():
    if 'emo' in comment.body:
        words = comment.body.split(' ')
        if words[0] == 'emo':
            print(comment.body)
            print(words)
            ans = emojy(words)
            print(ans)
            comment.reply(ans)
            time.sleep(15)

