import json
import random

key = ("Your",)

async def yourMom(message):
    options = ["**MMMMMMMMMMMMMMMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMMMM**",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)