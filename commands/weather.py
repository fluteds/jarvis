import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import config
import requests

def get_weather(command):
    city = extract_city(command)
    if city:
        api_key = config.OPENWEATHERMAP_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            return f"The weather in {city} is {weather_desc}. Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
        else:
            return "Sorry, I couldn't fetch the weather information."
    else:
        return "Sorry, I couldn't recognize the city name."

def extract_city(command):
    # Extract city name from command
    city = None
    if 'weather' in command:
        city = command.split('weather', 1)[1].strip()
    elif 'what\'s the weather in' in command:
        city = command.split('what\'s the weather in', 1)[1].strip()
    return city
