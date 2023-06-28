import requests
import pandas as pd
import datetime

API_KEY = '135dd2bd94df391d40c1b49f4eecf562'
weather_df = pd.DataFrame()

def get_location():
    zipcode = input('Enter your zip code: ')
    countrycode = input('Enter your country code: ')

    geocode_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{countrycode}&appid={API_KEY}'

    geocode_response = requests.get(geocode_url)

    lat = geocode_response.json().get('lat')
    lon = geocode_response.json().get('lon')
    return [lat, lon]
def get_weather():
    global weather_df
    location = get_location()
    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={location[0]}&lon={location[1]}&exclude=minutely,daily&appid={API_KEY}&units=imperial"

    weather_response = requests.get(weather_url)
    time={}
    count = 0
    for hour in weather_response.json().get('hourly'):
        hour['dt'] =  datetime.datetime.fromtimestamp(hour['dt'])
        time[count] = hour 
        count += 1
    weather_df = pd.DataFrame.from_dict(time, orient='index')
    print_header('weather in chicago')
    print(weather_df[['dt', 'temp', 'feels_like','pop']].head(12))
# Format text to look like header
def print_header(title):
    print(f'\n{title}')
    print('-' * len(title))


menu = {}
menu['1']="Descriptions" 
menu['2']="Wind speed"
menu['3']="Humidity"
menu['4']="Enter New Location"
get_weather()
while True: 
    options=menu.keys()
    for entry in options: 
        print(f'{entry}: {menu[entry]}')

    selection=input("Please Select:") 
    if selection =='1': 
        for row in weather_df['weather'].head(12).values:
            print(f'{row[0]["main"]} {row[0]["description"]}')     
    elif selection == '2': 
        print(weather_df['wind_speed'].head(12))
    elif selection == '3':
        print(weather_df['humidity'].head(12)) 
    elif selection == '4': 
        get_weather()
    else: 
        print() 


