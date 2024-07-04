import json
import random

key = ("Grubo",)
chudy = "<@388758898896797716>"

async def grubo(message):
    options = [chudy,]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)