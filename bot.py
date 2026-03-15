import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import discord


load_dotenv()
#print(os.getenv("DISCORD_TOKEDISCORD_TOKENN"))
TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)

CHANNEL_ID = 1099813364647088178
intents = discord.Intents.default()
intents.message_content = False
bot = commands.Bot(command_prefix="!",intents=intents)

async def weekly_greeting():
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            greeting_message = """
            🌞 Good morning, afternoon, or evening BlackPythonDevs
🌞 Buenos días, buenas tardes o buenas noches BlackPythonDevs
🌞 God morgen, god ettermiddag eller god kveld BlackPythonDevs 
🌞 Bonjour, bon après-midi ou bonsoir BlackPythonDevs
🌞 Guten Morgen, guten Tag oder guten Abend BlackPythonDevs
🌞 सुप्रभात, शुभ दोपहर या शुभ संध्या BlackPythonDev
🌞 Bom dia, boa tarde ou boa noite BlackPythonDevs
🌞 Ohayō, konnichiwa, mata wa konbanwa BlackPythonDevs
🌞 Buongiorno, buon pomeriggio o buonasera BlackPythonDevs
🌞 Dzień dobry lub dobry wieczór BlackPythonDevs
🌞 Dobro jutro, dobar dan ili dobro veče BlackPythonDevs
🌞 صباح الخير، مساء الخير BlackPythonDevs
🌞 Ẹ káàárọ̀, Ẹ káàsán, Ẹ káalẹ́ BlackPythonDevs
🌞 Günaydın, iyi günler veya iyi akşamlar BlackPythonDevs
🌞 Goedemorgen, goedemiddag of goedenavond BlackPythonDevs

☕ 🍵 ☕ 🍵 ☕ 🍵 ☕ 🍵 ☕ 🍵
            """
            await channel.send(greeting_message)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

    #initializing scheduler
    scheduler = AsyncIOScheduler()

    #Schedule weekly on Sundays at 12AM
    scheduler.add_job(weekly_greeting, "cron", day_of_week="sun", hour=00, minute=0) 

    #Temporary test: run now for testing
    asyncio.create_task(weekly_greeting())

    #starting the scheduler
    scheduler.start()

bot.run(TOKEN)

print(TOKEN)
