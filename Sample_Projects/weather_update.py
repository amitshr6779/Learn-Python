from types import CoroutineType
import requests
from pprint import pprint
API = ''
city = input("Enter City ")
URL = 'https://openweathermap.org/data/2.5/weather?apiid='+API+"+q="+city 
data = requests.get(URL)
pprint(data)
