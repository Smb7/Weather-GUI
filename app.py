import requests

# api key 
api_key = "7a2e90657fb7f49c0165d9565df9efac"

# base url 
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# city name
city_name = input("Enter City name: ")

# complete URL
complete_url = base_url + 'q=' + city_name + '&appid=' + api_key

# Send GET request to API 
response = requests.get(complete_url)

# Convert into JSON data
data = response.json()

# Check if response is successful
if data["cod"] != 404:
    # extract weather data
    weather_data = data["main"]
    temperature = weather_data["temp"]
    humidity = weather_data["humidity"]
    pressure = weather_data["pressure"]

    # printing data
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
else:
    print("404 Not Found")