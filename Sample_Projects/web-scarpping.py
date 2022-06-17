import imp
import requests
from bs4 import BeautifulSoup as bs

name = input("Enter username of your github: ")
URL = "https://github.com/"+name
req = requests.get(URL)
soup = bs(req.content, 'html.parser')
image = soup.find('img', {'alt' : 'Avatar'})['src']
print(image)