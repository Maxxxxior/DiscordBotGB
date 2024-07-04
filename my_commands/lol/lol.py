import json
import random

key = ("lol?",)

async def lol(message):
    options = ["lol beka z ciebie", ]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)