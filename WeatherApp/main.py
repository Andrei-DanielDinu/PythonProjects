import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        weather_info = f"City: {weather_data['name']}\n"\
                       f"Temperature: {weather_data['main']['temp']}°C\n"\
                       f"Weather: {weather_data['weather'][0]['description']}\n" \
                       f"Humidity: {weather_data['main']['humidity']}%\n"\
                       f"Wind Speed: {weather_data['wind']['speed']} m/s"
        result_label.config(text=weather_info)
    else:
        result_label.config(text="City not found")

root = tk.Tk()
root.title("Weather App")

# Styling
root.configure(bg="#e6f7ff")  # Background color
root.geometry("300x200")  # Window size

label_font = ('Arial', 12)  # Font for labels
entry_font = ('Arial', 11)  # Font for entry field
button_font = ('Arial', 11, 'bold')  # Font for button
result_font = ('Arial', 11)  # Font for result label

city_label = tk.Label(root, text="Enter city:", font=label_font, bg="#e6f7ff")
city_label.pack()

city_entry = tk.Entry(root, font=entry_font)
city_entry.pack()

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather, font=button_font, bg="#80bfff", fg="white")
get_weather_btn.pack()

result_label = tk.Label(root, text="", font=result_font, bg="#e6f7ff", wraplength=250)
result_label.pack()

root.mainloop()
