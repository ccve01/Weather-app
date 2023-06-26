import requests
//test
API_KEY = '135dd2bd94df391d40c1b49f4eecf562'

weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API_KEY}"
geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q=Beaumont,CA,US&appid={API_KEY}'

weather_response = requests.get(weather_url)
geocode_response = requests.get(geocode_url)

print("Geo Code")
print(geocode_response.status_code)
print(geocode_response.json())

print("Weather")
print(weather_response.status_code)
print(weather_response.json())

