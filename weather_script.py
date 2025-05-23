# Fetch weather data from OpenWeatherMap API,
import requests
import os

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print(f"Failed to get weather data for {city}. Error code: {response.status_code}")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    if not api_key:
        print("Error: API key is required.")
        exit(1)
    city = input("Enter city name: ")
    get_weather(city, api_key)



