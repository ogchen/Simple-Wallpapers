import requests
import json
import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def change_wallpaper():
    if os.path.isfile('image.jpg'):
        os.remove('image.jpg')

    r = requests.get('https://www.reddit.com/r/wallpaper+wallpapers/hot/.json', headers = {'User-agent': 'Simple Wallpapers bot'})
    try:
        r.raise_for_status()
    except Exception as exc:
        print('Error accessing Reddit API: %s' % (exc))

    data = r.json()
    url = data['data']['children'][0]['data']['url']
    url = url.replace('amp;', '')


    image = requests.get(url)
    try:
        image.raise_for_status()
    except Exception as exc:
        print('Error accessing image: %s' % (exc))

    with open('image.jpg', 'wb') as handler:
        handler.write(image.content)

    os.system("./SimpleWallpapers")

    time.sleep(10)

    dir_path = os.path.dirname(os.path.realpath(__file__))

    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + dir_path + "/image.jpg") #Background does not always change without this line
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + dir_path + "/wallpaper.jpg")

change_wallpaper()
scheduler = BlockingScheduler()
scheduler.add_job(change_wallpaper, 'interval', hours=0.01)
scheduler.start()
