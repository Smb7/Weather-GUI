import requests
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
import os  

# Needed for .env (access to API/ API URL)
load_dotenv()

# STEP1 Create class for out add
class WeatherApp:
    # init will create the GUI 
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App") # name of the app
        self.root.geometry('500x500') # size of the window
    
        # Photo
        self.city_label = tk.Label(self.root, text="Welcome to the Weather App")
        self.city_label.pack()

        # Create label and city entry
        self.city_label = tk.Label(self.root, text="Enter city name: ")
        self.city_label.pack()

        self.city_entry = tk.Entry(self.root, width=25)
        self.city_entry.pack()

        # Create button to fetch weather
        self.get_weather_button = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        # label to print results
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack()
    
    # STEP 2 Create API connection and run a response check
    def get_weather(self):

        # Get city name from entry widget
        city_name = self.city_entry.get()

        # api key 
<<<<<<< HEAD
        api_key = "Redacted"
=======
        api_key = os.getenv('API_KEY')
>>>>>>> aa6fab6 (add gitignore and updated API key)

        # base url 
        base_url = os.getenv('API_URL')

        # complete URL
        complete_url = base_url + 'q=' + city_name + '&units=metric&appid=' + api_key

        # Send GET request to API 
        response = requests.get(complete_url)

        # Convert into JSON data
        data = response.json()

        # Check if response is successful
        if data["cod"] != 200:
            print("404 Error! Not Found!")
            messagebox.showerror("Error", f"Failed to retrieve data: {data.get('message', 'Unknown Error')}")
        else:
            # extract weather data
            weather_data = data["main"]
            temperature = weather_data["temp"]
            humidity = weather_data["humidity"]
            pressure = weather_data["pressure"]
            self.result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa")

# Create main window
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
