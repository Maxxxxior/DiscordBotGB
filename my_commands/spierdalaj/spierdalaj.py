import random

key = ("spierdalaj",)

async def spierdalaj(message):
    options = ["Nie bo Ty","Nawzajem 🤗",]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)