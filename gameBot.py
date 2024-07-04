#main
import discord
from my_commands import gra

#import komend
#region importy
from my_commands.greetings.add_greeting import add_greeting
from my_commands.greetings.change_greeting import change_greeting
from my_commands.greetings.delete_greeting import delete_greeting
from my_commands.greetings.show_greetings import show_greetings
from my_commands.greetings.greeting import greeting
from my_commands.essa.essa import essa, landryna, hentaiToo, odklejka, lewdNekoPls, key as essa_key, key2 as landryna_key, key3 as hentaiToo_key, key4 as odklejka_key, lewdNeko as lewdNekoPls_key
from my_commands.mama.mama import mama, key as mama_key
from my_commands.isWorking.isWorking import isWorking, key as isWorking_key
from my_commands.zaimplementowanePomysly.zaimplementowanePomysly import zaimplementowanePomysly, key as zaimplementowanePomysly_key
from my_commands.wiekiWiekow.wiekiWiekow import wiekiWiekow, key as wiekiWiekow_key
from my_commands.ideas.ideas import ideas, key as ideas_key
from my_commands.sus.sus import sus, key as sus_key
from my_commands.hamburger.hamburger import hamburger, key as hamburger_key
from my_commands.lol.lol import lol, key as lol_key
from my_commands.imagod.imagod import imagod, key as imagod_key
from my_commands.nie.nie import nie, key as nie_key
from my_commands.dududupson.dududupson import dududupson, key as dududupson_key
from my_commands.panda.panda import panda, key as panda_key
from my_commands.yourMom.yourMom import yourMom, key as yourMom_key
from my_commands.grubo.grubo import grubo, key as grubo_key
from my_commands.tellMeWhy.tellMeWhy import tellMeWhy, key as tellMeWhy_key
from my_commands.ugaBuga.ugaBuga import ugaBuga, key as ugaBuga_key
from my_commands.spierdalaj.spierdalaj import spierdalaj, key as spierdalaj_key
#endregion

bot = discord.Client(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_message(message):
    #region hentaiToo
    if message.content.lower().startswith(hentaiToo_key):
        await hentaiToo(message)
    #endregion
    if message.author.bot:
        return
    #region COMMANDS
    #region !gra
    if message.content.startswith("!gra"):
        await gra.start_game(message)
    #endregion
    #region przywitania
    if message.content.startswith("!dodajPrzywitanie"):
        await add_greeting.add_greeting(message)
    elif message.content.startswith('!pokazPrzywitania'):
        await show_greetings.show_greetings(message)
    elif message.content.startswith('!zmienPrzywitanie'):
        await change_greeting.change_greeting(message)
    elif message.content.startswith("!usunPrzywitanie"):
        await delete_greeting.delete_greeting(message)
    else:
        await greeting.greeting(message)
    #endregion
    #region essa
    if message.content.lower().startswith(essa_key):
        await essa(message)
    #endregion
    #region landryna
    if message.content.lower().startswith(landryna_key):
        await landryna(message)
    #endregion
    #region odklejka
    if message.content.lower().startswith(odklejka_key):
        await odklejka(message)
    #endregion
    #region lewdNekoPls
    if message.content.lower().startswith(lewdNekoPls_key):
        await lewdNekoPls(message)
    #endregion
    #region MAMAAAAAAAA
    if message.content.lower().startswith(tuple(word.lower() for word in mama_key)):
        await mama(message)
    #endregion
    #region is working?
    if message.content.lower().startswith(tuple(word.lower() for word in isWorking_key)):
        await isWorking(message)
    #endregion
    #region wieki wieków amen
    if message.content.lower().startswith(tuple(word.lower() for word in wiekiWiekow_key)):
        await wiekiWiekow(message)
    #endregion
    #region ideas
    if message.content.lower().startswith(tuple(word.lower() for word in ideas_key)):
        await ideas(message)
    #endregion
    #region sus
    if message.content.lower().startswith(tuple(word.lower() for word in sus_key)):
        await sus(message)
    #endregion
    #region hamburger
    if message.content.lower().startswith(tuple(word.lower() for word in hamburger_key)):
        await hamburger(message)
    #endregion
    #region zaimplementowane pomysły
    if message.content.lower().startswith(tuple(word.lower() for word in zaimplementowanePomysly_key)):
        await zaimplementowanePomysly(message)
    #endregion
    #region lol
    if message.content.lower().startswith(tuple(word.lower() for word in lol_key)):
        await lol(message)
    #endregion
    #region imagod
    if message.content.lower().startswith(tuple(word.lower() for word in imagod_key)):
        await imagod(message)
    #endregion
    #region nie
    if message.content.lower().startswith(tuple(word.lower() for word in nie_key)):
        await nie(message)
    #endregion
    #region dududupson
    if message.content.lower().startswith(tuple(word.lower() for word in dududupson_key)):
        await dududupson(message)
    #endregion
    #region panda
    if message.content.lower().startswith(tuple(word.lower() for word in panda_key)):
        await panda(message)
    #endregion
    #region yourMom
    if message.content.lower().startswith(tuple(word.lower() for word in yourMom_key)):
        await yourMom(message)
    #endregion
    #region grubo
    if message.content.lower().startswith(tuple(word.lower() for word in grubo_key)):
        await grubo(message)
    #endregion
    #region tellMeWhy
    if message.content.lower().startswith(tuple(word.lower() for word in tellMeWhy_key)):
        await tellMeWhy(message)
    #endregion
    #region ugaBuga
    if message.content.lower().startswith(tuple(word.lower() for word in ugaBuga_key)):
        await ugaBuga(message)
    #endregion
    #region spierdalaj
    if message.content.lower().startswith(tuple(word.lower() for word in spierdalaj_key)):
        await spierdalaj(message)
    #endregion
    #endregion
    
#region SLASH przywitania
# @bot.command()
# async def dodajPrzywitanie(ctx):
#     await add_greeting.add_greeting(ctx.message)
# async def pokazPrzywitania(ctx):
#     await show_greetings.show_greetings(ctx.message)
# async def zmienPrzywitanie(ctx):
#     await change_greeting.change_greeting(ctx.message)
# async def usunPrzywitanie(ctx):
#     await delete_greeting.delete_greeting(ctx.message)
# #endregion

with open("token.txt") as f:
    token = f.read().strip()

bot.run(token)