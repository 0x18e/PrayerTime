import requests
import datetime
from bs4 import BeautifulSoup
from time import sleep
import pyfiglet
import random
from playsound import playsound
#halal
num = random.randint(0, 1)
font = ""
if num == 1:
    font = "starwars"
if num == 0:
    font = "speed"
result = pyfiglet.figlet_format("Prayer Timer", font=font)
print(result)
input("press enter to begin")
islamic_site = 'https://www.islamicfinder.org/world/kuwait/285787/kuwait-city-prayer-times/'
print("attempting get request")
with requests.session() as req:
    islamic_page = req.get(islamic_site)
    while(islamic_page.status_code == 400):
        sleep(2)
        islamic_page = req.get(islamic_site)
        print("working...")
    if islamic_page.status_code == 200:
        print("program running successfully")
        while True:
            sleep(1)
            currentTime = datetime.datetime.now().strftime("%I:%M %p")

            soup = BeautifulSoup(islamic_page.content, 'html.parser');

            prayer_table = soup.select("div.prayerTiles")
            '''
            fajr = prayer_table[0]
            dhuhr = prayer_table[2]
            asr = prayer_table[3]
            maghrib = prayer_table[4]
            isha = prayer_table[5]
            '''

            tableDict = {
                'fajr': prayer_table[0],
                'dhuhr': prayer_table[2],
                'asr': prayer_table[3],
                'maghrib': prayer_table[4],
                'isha': prayer_table[5],
            }
            for prayername, prayertime in tableDict.items():
                time = prayertime.select_one('.prayertime').text.strip()
                if (currentTime == time):
                    print(f'{time} {currentTime}')
                    print(f'TIME FOR {prayername} PRAYER')
                    playsound('azan1.mp3')


