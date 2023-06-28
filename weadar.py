import requests
import pandas as pd
API_KEY = '135dd2bd94df391d40c1b49f4eecf562'

zipcode = input('Enter your zip code: ')
countrycode = input('Enter your country code: ')

geocode_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{countrycode}&appid={API_KEY}'

geocode_response = requests.get(geocode_url)

print("Geo Code")
print(geocode_response.status_code)
print(geocode_response.json())

lat = geocode_response.json().get('lat')
lon = geocode_response.json().get('lon')

weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,daily&appid={API_KEY}&units=imperial"

weather_response = requests.get(weather_url)

print("Weather")
print(weather_response.status_code)
print(weather_response.json())



weather_df = pd.DataFrame()
time={}
count = 0
for hour in weather_response.json().get('hourly'):
    time[count] = hour 
    count += 1
weather_df = pd.DataFrame.from_dict(time, orient='index')
print(weather_df)