import json
import random

key = ("Uga Buga Łysy Chuju",)

async def ugaBuga(message):
    options = ["Uga Buga Łysy Kondomie",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)