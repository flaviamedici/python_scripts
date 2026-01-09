import requests

API_KEY = 'openweatherapikey123456'
CITY = 'Seattle'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_status():
    params = {
        'q': CITY,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Current weather in {CITY}: {weather}, Temperature: {temperature}°C")
    else:
        print("Error fetching weather data")
    return data
get_weather_status()

#check for specific weather condition and based on the words found, display a messgae to the user to let they know about the weather. 
# For example, if the description has the words rain, drizzle, display a message "Don't forget to bring an umbrella!". If the 
# description is snow, display a message " make sure you are bundled up", if the description has the word sun, hot, display a
#  message "Today is going to be nice and warm"
# make sure you have different messages for dififerent weather conditions.
def weather_advisory(weather_description):
    weather_description = weather_description.lower()
    if 'rain' in weather_description or 'drizzle' in weather_description:
        print("Don't forget to bring an umbrella!")
    elif 'snow' in weather_description:
        print("Make sure you are bundled up!")
    elif 'sun' in weather_description or 'hot' in weather_description:
        print("Today is going to be nice and warm!")
    elif 'cloud' in weather_description:
        print("It might be a bit gloomy today.")
    elif 'storm' in weather_description or 'thunder' in weather_description:
        print("Stay safe! Severe weather conditions expected.")
    elif 'fog' in weather_description or 'mist' in weather_description:
        print("Drive carefully! Low visibility due to fog.")
    elif 'wind' in weather_description:
        print("It's going to be windy today, hold onto your hats!")

data = get_weather_status()
weather_description = data['weather'][0]['description']
weather_advisory(weather_description)

