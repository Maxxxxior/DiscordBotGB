import json
from config import GREETINGS_FILE_PATH

async def show_greetings(message):
    if message.content.startswith('pokazPrzywitania'):
            data = {}
            try:
                with open(GREETINGS_FILE_PATH, "r", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if data:
                        greetings = "Dostępne przywitania:\n```"
                        for key, value in data.items():
                            greetings += f"{key} - dodane przez @{value['author']} [{value['author_id']}]\n"
                        greetings += "```"
                        await message.channel.send(greetings)
                    else:
                        await message.channel.send("Nie ma żadnych przywitań.")
            except:
                await message.channel.send("Nie ma żadnych przywitań.")