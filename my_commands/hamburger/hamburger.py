# import json
# import random
# import discord

# # key = ("Czemu {} nie może zjeść hamburgera",)
# async def on_message(message):
#     user_input = message.content.lower()
#     key = f"Czemu {user_input} nie może zjeść hamburgera"
# # key = key.format(user_input)

# async def hamburger(message):
#     answerXD = "XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
#     options = ["Bo nie żyje ", ]
#     trimmedAnswerXD = answerXD[2:random.randrange(1,51)]
#     selected_option = random.choice(options)
#     await message.channel.send(f"{selected_option}{trimmedAnswerXD}")

import json
import random
import re

key = ("Czemu .* nie może zjeść hamburgera",)

async def hamburger(message):
    match = re.search(key[0], message.content)
    if match:
        quantity = random.randint(1,50)
        options = ["Bo nie żyje X" + "D" * quantity]
        selected_option = random.choice(options)
        await message.channel.send(selected_option)