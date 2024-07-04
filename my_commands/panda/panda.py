import json
import random

key = ("panda",)

async def panda(message):
    options = ["Kto?",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)