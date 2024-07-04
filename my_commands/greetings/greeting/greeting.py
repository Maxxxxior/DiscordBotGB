import json
from config import GREETINGS_FILE_PATH

async def greeting(message):
    with open(GREETINGS_FILE_PATH, "r", encoding="utf8") as json_file:
            data = json.load(json_file)
            for key in data.keys():
                if message.content.lower().startswith(key.lower()):
                    await message.channel.send("Hej co słychać?")