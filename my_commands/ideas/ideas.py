import json
import datetime
import re
from config import IDEAS_FILE_PATH

key = ("!addIdea", "!dodajPomysł", "!dodajPomysl")

async def ideas(message):
    # Pobieranie pomysłu i odpowiedzi z wiadomości
    idea = message.content.split("'")[1]
    answer = message.content.split("'")[3]
    
    # Pobieranie informacji o autorze i czasie dodania
    author = message.author.name
    author_id = message.author.id
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Pobieranie ostatniego numeru pomysłu z pliku
    with open(IDEAS_FILE_PATH, "r", encoding="utf8") as file:
        lines = file.readlines()
    if lines:
        last_idea = re.search("Idea\[(\d+)\]", lines[-1]).group(1)
        idea_number = int(last_idea) + 1
    else:
        idea_number = 1
    
    # Formatowanie danych do zapisu
    idea_data = f"Idea[{idea_number}] - {idea} >> {answer} - dodane przez {author} [{author_id}] o godzinie: {timestamp}"
    
    # Zapis danych do pliku
    with open(IDEAS_FILE_PATH, "a", encoding="utf8") as file:
        file.write(idea_data + "\n")
    
    await message.channel.send("Pomysł zapisany!")