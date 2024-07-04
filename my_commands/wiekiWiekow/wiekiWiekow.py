import json
import random

key = ("niech będzie pochwalony jezus chrystus", "niech będzie pochwalony jezus chytrus", "niech będzie pochwalony jesus chrystus", "niech będzie pochwalony jesus chytrus")

async def wiekiWiekow(message):
    options = ["Na wieki wieków amen", "Na wieki wieków ramen", ]
    selected_option = random.choice(options)
    await message.channel.send(selected_option)
    if "ramen" in selected_option:
        await message.add_reaction("🍜")
    elif "amen" in selected_option:
        await message.add_reaction("🙏")