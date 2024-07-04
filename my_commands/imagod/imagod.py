import json
import random

key = ("Jestem..",)

async def imagod(message):
    options = ["...Bogiem, uświadom to sobie sobie", "...Pedałem"]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)