import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=b140f44f1fb34ad58ca213644250106&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
describtion = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, 'is', describtion, 'and', temp, 'degree')

 

