import emoji
import random

options = [ emoji.UNICODE_EMOJI_ENGLISH, emoji.UNICODE_EMOJI_ALIAS_ENGLISH,
            emoji.UNICODE_EMOJI_ITALIAN,emoji.UNICODE_EMOJI_SPANISH,
            emoji.UNICODE_EMOJI_PORTUGUESE  ]

choi = random.choice(options)

emo = []
for i in choi:
    emo.append(i)

with open('text.txt',encoding="utf-8") as file:
    f = file.read()

words = f.split(' ')

ans = ''
for w in words:
    # print(w,' ',random.choice(emo))
    ans += w + ' ' + random.choice(emo)

print(ans)

f = open('answer.txt', 'w', encoding="utf-8")
f.write(str(ans))
