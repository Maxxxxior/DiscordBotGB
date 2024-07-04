import json
from config import GREETINGS_FILE_PATH

async def add_greeting(message):
    if message.content.startswith('!dodajPrzywitanie'):
            # split the message content to get the greeting
            words = message.content.split(' ')
            if len(words) < 2:
                await message.channel.send("Nie podano przywitania do dodania.")
                return
            greeting = words[1]
            data = {}
            try:
                with open(GREETINGS_FILE_PATH, "r", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    data[greeting] = {"author": message.author.name, "author_id": message.author.id}
            except:
                data[greeting] = {"author": message.author.name, "author_id": message.author.id}
            
            with open(GREETINGS_FILE_PATH, "w", encoding="utf8") as json_file:
                json.dump(data, json_file)
            
            await message.channel.send(f'Dodano przywitanie "{greeting}"')