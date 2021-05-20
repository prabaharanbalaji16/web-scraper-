import pandas as p
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.91980696400003&lon=-86.28179348799995#.YKXNS6hKjIU')
soup = BeautifulSoup(page.content,"html.parser")
weeks = soup.find(id="seven-day-forecast-body")
items = weeks.find_all(class_="tombstone-container")
# print(items[0].find(class_="period"))

period_names = [item.find(class_="period-name").getText() for item in items]
desc = [item.find(class_="short-desc").getText() for item in items]
temp = [item.find(class_="temp").getText() for item in items]

weather = p.DataFrame({
    "Period":period_names,
    "Description":desc,
    "Temperature":temp,
})

weather.to_html('index.html')