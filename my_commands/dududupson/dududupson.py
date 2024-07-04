import json
import random

key = ("DUDUDUPSON",)

async def dududupson(message):
    options = ["DUDNIĄ MI PLEMNIKI W JAJACH",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)