import datetime
from datetime import *

BossTable = [
    {"ID": 1, "Day": 0, "Hour": 0, "Minute": 15, "Name": "Karanda-Kutum", "Notification": True, "Color": 0x66ff33},
    {"ID": 2, "Day": 0, "Hour": 2, "Minute": 0, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 3, "Day": 0, "Hour": 5, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 4, "Day": 0, "Hour": 9, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 5, "Day": 0, "Hour": 12, "Minute": 0, "Name": "Offin", "Notification": True, "Color": 0xff0000},
    {"ID": 6, "Day": 0, "Hour": 16, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 7, "Day": 0, "Hour": 19, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 8, "Day": 0, "Hour": 22, "Minute": 15, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},

    {"ID": 9, "Day": 1, "Hour": 0, "Minute": 15, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 10, "Day": 1, "Hour": 2, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 11, "Day": 1, "Hour": 5, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 12, "Day": 1, "Hour": 9, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 13, "Day": 1, "Hour": 12, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 14, "Day": 1, "Hour": 16, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 15, "Day": 1, "Hour": 19, "Minute": 0, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 16, "Day": 1, "Hour": 22, "Minute": 15, "Name": "Garmoth", "Notification": True, "Color": 0xff9900},

    {"ID": 17, "Day": 2, "Hour": 0, "Minute": 15, "Name": "Kutum-Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 18, "Day": 2, "Hour": 2, "Minute": 0, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 19, "Day": 2, "Hour": 5, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 20, "Day": 2, "Hour": 9, "Minute": 0, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 21, "Day": 2, "Hour": 16, "Minute": 0, "Name": "Kutum-Offin", "Notification": True, "Color": 0xff0000},
    {"ID": 22, "Day": 2, "Hour": 19, "Minute": 0, "Name": "Vell", "Notification": True, "Color": 0x00ffff},
    {"ID": 23, "Day": 2, "Hour": 22, "Minute": 15, "Name": "Karanda-Kzarka", "Notification": True, "Color": 0x66ff33},
    {"ID": 24, "Day": 2, "Hour": 23, "Minute": 15, "Name": "Quint-Muraka", "Notification": True, "Color": 0xff0000},

    {"ID": 25, "Day": 3, "Hour": 0, "Minute": 15, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 26, "Day": 3, "Hour": 2, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 27, "Day": 3, "Hour": 5, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 28, "Day": 3, "Hour": 9, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 29, "Day": 3, "Hour": 12, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 30, "Day": 3, "Hour": 16, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 31, "Day": 3, "Hour": 19, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 32, "Day": 3, "Hour": 22, "Minute": 15, "Name": "Garmoth", "Notification": True, "Color": 0xff9900},

    {"ID": 33, "Day": 4, "Hour": 0, "Minute": 15, "Name": "Kzarka-Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 34, "Day": 4, "Hour": 2, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 35, "Day": 4, "Hour": 5, "Minute": 0, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 36, "Day": 4, "Hour": 9, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 37, "Day": 4, "Hour": 12, "Minute": 0, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 38, "Day": 4, "Hour": 16, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 39, "Day": 4, "Hour": 19, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 40, "Day": 4, "Hour": 22, "Minute": 15, "Name": "Kutum-Kzarka", "Notification": True, "Color": 0xff0000},

    {"ID": 41, "Day": 5, "Hour": 0, "Minute": 15, "Name": "Karanda", "Notification": True, "Color": 0x66ff33},
    {"ID": 42, "Day": 5, "Hour": 2, "Minute": 0, "Name": "Offin", "Notification": True, "Color": 0xff0000},
    {"ID": 43, "Day": 5, "Hour": 5, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 44, "Day": 5, "Hour": 9, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 45, "Day": 5, "Hour": 12, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 46, "Day": 5, "Hour": 16, "Minute": 0, "Name": "Quint-Muaraka", "Notification": True, "Color": 0xff0000},
    {"ID": 47, "Day": 5, "Hour": 19, "Minute": 0, "Name": "Karanda-Kzarka", "Notification": True, "Color": 0x66ff33},

    {"ID": 48, "Day": 6, "Hour": 0, "Minute": 15, "Name": "Nouver-Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 49, "Day": 6, "Hour": 2, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 50, "Day": 6, "Hour": 5, "Minute": 0, "Name": "Kutum", "Notification": True, "Color": 0xff0000},
    {"ID": 51, "Day": 6, "Hour": 9, "Minute": 0, "Name": "Nouver", "Notification": True, "Color": 0xff0000},
    {"ID": 52, "Day": 6, "Hour": 12, "Minute": 0, "Name": "Kzarka", "Notification": True, "Color": 0xff0000},
    {"ID": 53, "Day": 6, "Hour": 16, "Minute": 0, "Name": "Vell", "Notification": True, "Color": 0x00ffff},
    {"ID": 54, "Day": 6, "Hour": 19, "Minute": 0, "Name": "Garmoth", "Notification": True, "Color": 0xff9900},
    {"ID": 55, "Day": 6, "Hour": 22, "Minute": 15, "Name": "Kzarka-Nouver", "Notification": True, "Color": 0xff0000},
]


async def findNextBossOnStart():
    Now = datetime.now()
    for Data in BossTable:

        # Dziś
        if Now.weekday() == Data["Day"] and Now.hour <= Data["Hour"]:
            return Data["ID"]


    print("Dzien: " + str(Now.weekday()))
    print("Godzina: " + str(Now.hour))

Boss = False

async def getTimetoNextBoss(BossID):
    for Data in BossTable:
        if BossID == Data["ID"]:
            Boss = Data
            break

    Now = datetime.now()

    if Now.weekday() == Boss["Day"]:
        BossTime = datetime(Now.year, Now.month, Now.day, Boss["Hour"], Boss["Minute"])
        #print("Dziś")
    else:
        BossTime = datetime(Now.year, Now.month, Now.day, Boss["Hour"], Boss["Minute"]) + timedelta(days=1)
        #print("Jutro")

    TimeToBoss = BossTime - Now
    TimeToBoss_Minutes = int(divmod(TimeToBoss.total_seconds(), 60)[0] + 1)

    return TimeToBoss_Minutes

async def nextBossInfo(BossID):
    for Data in BossTable:
        if BossID == Data["ID"]:
            Boss = Data
            break

    return Boss