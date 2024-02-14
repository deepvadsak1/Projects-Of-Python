import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Unable to fetch weather information.")

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)
