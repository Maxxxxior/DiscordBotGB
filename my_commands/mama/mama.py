import json
import random

key = ("mama","mamma")

async def mama(message):
    options = ["Oooooooh 🎵🎵🎵","UuuUUuuuu 🎵🎵🎵","OooOooOOoo 🎵🎵🎵"]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)