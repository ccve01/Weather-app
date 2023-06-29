import requests
import pandas as pd
import datetime

API_KEY = '135dd2bd94df391d40c1b49f4eecf562'
weather_df = pd.DataFrame()
City_name = 'Spot'

def get_zipcode(text):
    return input(text)

def get_countrycode(text):
    return input(text)

def get_location(zip, country):
        global City_name

        zipcode = zip
        countrycode = country

        geocode_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{countrycode}&appid={API_KEY}'

        geocode_response = requests.get(geocode_url)

        lat = geocode_response.json().get('lat')
        lon = geocode_response.json().get('lon')
        City_name = geocode_response.json().get('name')
        return [lat, lon]

def get_weather():
        global weather_df
        location = get_location(get_zipcode('Enter Zip Code: '), get_countrycode('Enter Country Code: '))
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={location[0]}&lon={location[1]}&exclude=minutely,daily&appid={API_KEY}&units=imperial"

        weather_response = requests.get(weather_url)
        time={}
        count = 0
        for hour in weather_response.json().get('hourly'):
            hour['dt'] =  datetime.datetime.fromtimestamp(hour['dt'])
            time[count] = hour 
            count += 1
        weather_df = pd.DataFrame.from_dict(time, orient='index')
        print_header(City_name)
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
menu['5']="Exit"
print_header("Enter your location")
get_weather()
while True: 
        options=menu.keys()
        print_header('Menu Options')
        for entry in options: 
            print(f'{entry}: {menu[entry]}')

        selection=input("Please Select:") 
        if selection =='1': 
            cast ={}
            print_header("Today's Overcast")
            for row in weather_df[['dt','weather']].head(12).values: 
                cast[row[0]] = {'main':row[1][0]["main"], 'description':row[1][0]["description"]}
                cast_df = pd.DataFrame.from_dict(cast, orient='index')
            print(cast_df) 
        elif selection == '2': 
            print_header("Today's Windspeed")
            print(weather_df[['dt','wind_speed']].head(12))
        elif selection == '3':
            print_header("Humidity for today")
            print(weather_df[['dt','humidity']].head(12)) 
        elif selection == '4': 
            print_header("Enter New Location:")
            get_weather()
        elif selection == '5':
            break
        else: 
            print() 
