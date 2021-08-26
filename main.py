# bot.py
import os
import discord
import asyncio
from dotenv import load_dotenv

from boss import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    prevTimetoNext = False
    nextBossID = False
    avatarPath = False

    while True:
        if not nextBossID:
            nextBossID = await findNextBossOnStart()

        TimetoNext = await getTimetoNextBoss(nextBossID)
        nextBoss = await nextBossInfo(nextBossID)

        if TimetoNext != prevTimetoNext:
            prevTimetoNext = TimetoNext

            print("Kolejny boss: " + str(nextBossID))

            # Discord Status
            Text = nextBoss["Name"] + " za " + str(TimetoNext) + "min"
            activity = discord.Game(name=Text, type=3)
            await client.change_presence(activity=activity)

            print(f'{client.user} has connected to Discord!')
            print(f'{nextBoss["Name"]} to nastepny boss! Za ' + str(TimetoNext) + 'min')

            # Discord Avatar
            if not avatarPath or avatarPath != '"PNG/"+ str(nextBoss["Name"]) +".png"':
                path = "PNG/"+ str(nextBoss["Name"]) +".png"
                file_path = open(path, 'rb')
                avatar = file_path.read()
                await client.user.edit(avatar=avatar)

            # Discord Messega
            if TimetoNext == 15 and nextBoss["Notification"] == True:
                channel = client.get_channel(os.getenv('DISCORD_BOSSTIMER_CHANNEL'))

                embedVar = discord.Embed(title="Boss Timer", description="", color=nextBoss["Color"])
                embedVar.add_field(name="Kolejny boss", value=nextBoss["Name"], inline=True)
                embedVar.add_field(name="Pozostały czas", value=str(TimetoNext) + " min", inline=True)
                await channel.send(embed=embedVar)

            if TimetoNext < 0:
                nextBossID = nextBossID + 1
                if nextBossID > 55:
                    nextBossID = 1

        # Timer
        await asyncio.sleep(5)


client.run(TOKEN)
