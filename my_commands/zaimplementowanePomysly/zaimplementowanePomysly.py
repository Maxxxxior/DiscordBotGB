import json
import datetime
import re
import math
from config import IDEAS_FILE_PATH

key = ("!wykonanePomysły", "!wykonanePomysly", "!zaimplementowanePomysły", "!zaimplementowanePomysly")

async def zaimplementowanePomysly(message):
    with open(IDEAS_FILE_PATH, "r", encoding="utf8") as file:
        lines = file.readlines()
        
    all_ideas = len(lines)
    done_ideas = 0
    for line in lines:
        if "zaimplementowano" in line:
            done_ideas += 1
    
    # procentowa wartość w zaokrągledniu do liczby całkowitej
    percentage = math.ceil((done_ideas/all_ideas) * 100)
    if percentage == 100:
        await message.channel.send(f"Aktualnie zaimplementowano {done_ideas} z {all_ideas} pomysłów. Jest to {percentage}% wszystkich pomysłów! 😎🤙")
    elif percentage >= 80:
        await message.channel.send(f"Aktualnie zaimplementowano {done_ideas} z {all_ideas} pomysłów. Jest to {percentage}% wszystkich pomysłów! 😎")
    elif percentage >= 60:
        await message.channel.send(f"Aktualnie zaimplementowano {done_ideas} z {all_ideas} pomysłów. Jest to {percentage}% wszystkich pomysłów! 😝")
    elif percentage >= 50:
        await message.channel.send(f"Aktualnie zaimplementowano {done_ideas} z {all_ideas} pomysłów. Jest to {percentage}% wszystkich pomysłów! 😅")
    elif percentage < 50:
        await message.channel.send(f"Aktualnie zaimplementowano {done_ideas} z {all_ideas} pomysłów. Jest to {percentage}% wszystkich pomysłów! 😭")