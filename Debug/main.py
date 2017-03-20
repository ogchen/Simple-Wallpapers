import requests
import json
import os

if os.path.isfile('image.jpg'):
    os.remove('image.jpg')

if os.path.isfile('wallpaper.jpg'):
    os.remove('wallpaper.jpg')

r = requests.get('https://www.reddit.com/r/wallpapers/top/.json', headers = {'User-agent': 'Simple Wallpapers bot'})
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

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.system("gsettings set org.gnome.desktop.background picture-uri file://" + dir_path + "/wallpaper.jpg")

