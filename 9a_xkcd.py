import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

xkcd_url = 'https://xkcd.com'

download_directory = 'xkcd_comics'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

source_code = requests.get(xkcd_url).text

soup = BeautifulSoup(source_code, 'html.parser')

comic_elements = soup.find_all('img')

for comic_element in comic_elements:
    
    comic_image_url = urljoin(xkcd_url, comic_element['src'])
    
    img_response = requests.get(comic_image_url)
    
    image_filename = os.path.join(download_directory, os.path.basename(comic_image_url)) 
    
    with open(image_filename, 'wb') as img_file:
        img_file.write(img_response.content)

    print("Downloaded:", image_filename)

print("All XKCD comics downloaded successfully!")
