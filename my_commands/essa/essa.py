import requests
import random

key = ("essa","ez",)
key2 = ("landryna",)
key3 = ("yes i do",)
key4 = ("odklejka",)
lewdNeko = ("lewd neko pls",)

async def essa(message):
    await message.add_reaction("😎")
    await message.add_reaction("🤙")
    
async def landryna(message):
    await message.add_reaction("🥰")
    await message.channel.send("Słucham skarbie?")
    
async def hentaiToo(message):
    await message.channel.send("Hentai too hehe")
    
async def odklejka(message):
    await message.channel.send("<@269187438910373912>")
    
async def lewdNekoPls(message):
    numbers = list(range(1, 1000)) # lista z numerami zdjęć
    random.shuffle(numbers)
    for number in numbers:
        url = f"https://nekos.fun/storage/lewd/lewd_neko{number}.jpg"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                await message.channel.send(url)
                return
        except:
            pass
    await message.channel.send("Sorry, I couldn't find any images.")
        # response = requests.get(url)
        # if response.status_code == 200:
        #     # zdjęcie istnieje, więc wysyłamy na kanał
        #     await message.channel.send(url)
        #     break
        # else:
        #     # jeśli przeszliśmy przez całą listę bez znalezienia zdjęcia
        #     await message.channel.send("Nie znaleziono żadnego zdjęcia.")