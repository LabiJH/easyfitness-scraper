from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os
import discord
import asyncio
import dotenv

load_dotenv()
TOKEN= os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1212116811534045237
intents = discord.Intents.all() 
client = discord.Client(intents=intents)
URL = "https://easyfitness.club/studio/easyfitness-bornheim/"

async def send_updates():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    meterbubble = soup.find_all("span", class_="meterbubble")
    firstBubble = meterbubble[0] # for some reason there are TWO bubble Objects?
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    
    while True:
        await channel.send("Das Studio hat " + firstBubble.text + " Auslastung momentan")
        await asyncio.sleep(1800)  # Sleep for 30 minutes (1800 seconds)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await send_updates()  # Start sending updates when the bot is ready

client.run(TOKEN)