from discord.ext import commands 
import discord
from dataclasses import dataclass
import datetime
from uro_converter import urodzenia_dict 
import asyncio
import schedule
import time
import json
import os

if os.path.exists(os.getcwd()+ "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"token": "", "Prefix": "!"}

    with open(os.getcwd()+ "/config.json", "w+") as f:
        json.dump(configTemplate, f)


token = configData["token"]
prefix = configData["Prefix"]


CHANNEL_ID = 1095396174992773180

today = datetime.date.today()
year = today.year
month_day = today.strftime("%m-%d")
today_string = str(today)
year_str = str(year)
month_day_str = str(month_day)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


async def daily_task():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    uro_today = []
    for key in urodzenia_dict:
        if urodzenia_dict[key] == month_day_str:
            uro_today.append(key)
    if len(uro_today) > 0:
        uro_message = "Dziś urodziny obchodzą:\n"
        for u, w in uro_today:
            uro_message += f"{u} - {w} lat.\n"
        await channel.send(uro_message)
    else:
        pass
    
def schedule_task():
    schedule.every().day.at("18:48").do(asyncio.ensure_future, daily_task())

@bot.event
async def on_ready():
    print('zalogowano jako {0.user}'.format(bot))
    schedule_task()
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
   
bot.run(token)



