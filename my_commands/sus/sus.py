import json
import random

key = ("Sus?",)

async def sus(message):
    options = ["AMONGUS SUGOMA SUS IMPOSTOR AMOGUS", ]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)