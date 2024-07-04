import json
import random

key = ("Tell me why",)

async def tellMeWhy(message):
    options = ["AINT NOTHING BUT A HEARTACHEEEEEEEEEEE",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)