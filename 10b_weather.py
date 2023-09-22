import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = 'f2904eb657749d1c11fcf07d0ba4e0eb'
city = 'Mangalore'
units = '&units=metric'
url = base_url + 'q=' + city + '&appid=' + api_key + units
response = requests.get(url)
weather_data = response.json()
main_info = weather_data['main']
temperature = main_info['temp']
humidity = main_info['humidity']
pressure = main_info['pressure']
wind_info = weather_data['wind']
wind_speed = wind_info['speed']
weather_condition = weather_data['weather'][0]['description']
print('Temperature:', temperature, '\nHumidity:', humidity, '\nPressure:', pressure,
      '\nWind Speed:', wind_speed, '\nCloud Condition:', weather_condition)
