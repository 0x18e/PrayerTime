import requests
import datetime
from bs4 import BeautifulSoup
from time import sleep
import pyfiglet
import random
#halal
#test
num = random.randint(0, 1)
font = ""
if num == 1:
    font = "starwars"
if num == 0:
    font = "speed"
result = pyfiglet.figlet_format("Prayer Timer", font=font)
print(result)
islamic_site = 'https://www.islamicfinder.org/world/kuwait/285787/kuwait-city-prayer-times/'
with requests.session() as req:

    islamic_page = req.get(islamic_site)
    if islamic_page.status_code == 400:
        print("run program again")
    elif islamic_page.status_code == 200:
        while True:
            sleep(1)
            currentTime = datetime.datetime.now().strftime("%I:%M %p")

            soup = BeautifulSoup(islamic_page.content, 'html.parser');

            prayer_table = soup.select("div.prayerTiles")

            fajr = prayer_table[0]
            dhuhr = prayer_table[2]
            asr = prayer_table[3]
            maghrib = prayer_table[4]
            isha = prayer_table[5]


            tableDict = {
                'fajr': fajr,
                'dhuhr': dhuhr,
                'asr': asr,
                'maghrib': maghrib,
                'isha': isha,
            }
            for prayername, prayertime in tableDict.items():
                time = prayertime.select_one('.prayertime').text.strip()
                if (currentTime == time):
                    print(f'{time} {currentTime}')
                    print(f'TIME FOR {prayername} PRAYER')



