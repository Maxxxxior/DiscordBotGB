import json
import datetime
from datetime import datetime
from config import GREETINGS_FILE_PATH, GREETINGS_LOGS_FILE_PATH, MODERATOR_ROLE_ID, SZEF_ROLE_ID

async def delete_greeting(message):
    if message.content.startswith("!usunPrzywitanie"):
        # Sprawdź czy autor ma odpowiednią rolę administracyjną
        role_ids = [role.id for role in message.author.roles]
        rolaModerator = MODERATOR_ROLE_ID
        rolaSzef = SZEF_ROLE_ID
        if rolaModerator in role_ids or rolaSzef in role_ids:
            # Pobierz nazwę przywitania do usunięcia
            greeting_to_delete = message.content[16:]
            # Wczytaj plik greetings.json
            with open(GREETINGS_FILE_PATH, "r", encoding="utf8") as json_file:
                data = json.load(json_file)
            # Sprawdź czy przywitanie istnieje w pliku
            greeting_to_delete = message.content[16:].strip()
            if greeting_to_delete in data:
                del data[greeting_to_delete]
                # Zapisz zmiany do pliku greetings.json
                with open(GREETINGS_FILE_PATH, "w", encoding="utf8") as json_file:
                    json.dump(data, json_file)
                # Zapisz log
                with open(GREETINGS_LOGS_FILE_PATH, "a", encoding="utf8") as log_file:
                    log_file.write(f"[{datetime.now()}] User: {message.author.name} - Deleted: {greeting_to_delete} - From: greetings.json\n")
                # Wyślij komunikat o pomyślnym usunięciu przywitania
                await message.channel.send(f"Przywitanie {greeting_to_delete} zostało usunięte.")
            else:
                await message.channel.send(f"Przywitanie {greeting_to_delete} nie istnieje.")
        else:
            await message.channel.send("Nie masz uprawnień do usuwania przywitania.")