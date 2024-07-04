import json
import datetime
from datetime import datetime
from config import GREETINGS_FILE_PATH, GREETINGS_LOGS_FILE_PATH

async def change_greeting(message):
    if message.content.startswith('!zmienPrzywitanie'):
        try:
            # split the message content to get the old and new greeting
            old_greeting, new_greeting = message.content.split(' ')[1], message.content.split(' ')[2]
            data = {}
            with open(GREETINGS_FILE_PATH, "r", encoding="utf8") as json_file:
                data = json.load(json_file)
                if old_greeting in data.keys():
                    data[new_greeting] = data.pop(old_greeting)
                    data[new_greeting]["modified_by"] = message.author.name
                    data[new_greeting]["modified_by_id"] = message.author.id
                    with open(GREETINGS_FILE_PATH, "w", encoding="utf8") as json_file:
                        json.dump(data, json_file)
                    with open(GREETINGS_LOGS_FILE_PATH, "a", encoding="utf8") as log_file:
                        log_file.write(f"[{datetime.now()}] User: {message.author.name} - Modified: {old_greeting} to {new_greeting} - In: greetings.json\n")
                    await message.channel.send(f'Zmieniono przywitanie "{old_greeting}" na "{new_greeting}".')
                else:
                    await message.channel.send(f'Przywitanie "{old_greeting}" nie istnieje.')
        except ValueError:
            await message.channel.send("Niepoprawne użycie komendy. Użyj !zmienPrzywitanie <stare przywitanie> <nowe przywitanie>")