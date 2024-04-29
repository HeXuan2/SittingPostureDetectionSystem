import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.bing.com/images/search?q=%e5%ad%a6%e7%94%9f%e5%9d%90%e5%a7%bf%e5%9b%be%e7%89%87&qpvt=%e5%ad%a6%e7%94%9f%e5%9d%90%e5%a7%bf%e5%9b%be%e7%89%87&form=IGRE&first=1'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

img_elements = soup.find_all('img', class_='mimg')

img_urls = []

for img_element in img_elements:
    src = img_element.get('src')
    if src:
        img_urls.append(src)

if not os.path.exists('images'):
    os.mkdir('images')

for i, img_url in enumerate(img_urls):
    response = requests.get(img_url)
    with open(f'images/{i:03}.jpg', 'wb') as f:
        f.write(response.content)