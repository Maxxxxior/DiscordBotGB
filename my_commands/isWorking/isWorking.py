import json
import random

key = ("działa", "dziaua")

async def isWorking(message):
    options = ["https://tenor.com/view/hell-yeah-gif-24751671", "https://tenor.com/view/hulk-hogan-nodding-nod-yes-yup-gif-13973219", "https://tenor.com/view/baby-scream-yeah-hockey-kid-gif-24698394", "https://tenor.com/view/hell-yeah-yeah-oh-yeah-yes-hell-yes-gif-21504886", "https://tenor.com/view/dancing-boy-cowboy-gif-19597798", "https://tenor.com/view/oh-yeah-gif-23378792"]
    selected_option = random.choice(options)
    await message.add_reaction("✅")
    await message.channel.send(selected_option)