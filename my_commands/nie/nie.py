import json
import random

key = ("Nie","Nie wiem",)

async def nie(message):
    options = ["Nie wiem", "https://tenor.com/view/nie-wiem-papie%C5%BC-nie-wiem-pope-kid-gif-15617312",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)