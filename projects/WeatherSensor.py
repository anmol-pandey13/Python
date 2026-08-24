import random
from datetime import datetime

temperature = random.randint(20, 40)  # Simulated temperature in Celsius
humidity = random.randint(30, 70)     # Simulated humidity in percentage

print(f"Temperature: {temperature}°C\nHumidity: {humidity}%")

rainfall = random.randint(0, 100)

if rainfall > 70:
    weather = "Heavy Rain"
elif rainfall > 30:
    weather = "Light Rain"
else:
    weather = "Clear"

print(f"Rainfall: {rainfall} mm")
print(f"Weather: {weather}")

time = datetime.now().strftime("%H:%M:%S")
date= datetime.now().strftime("%Y-%m-%d")
print("----- Weather Sensor -----")
print(f"Date: {date}")
print(f"Time: {time}")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Rainfall: {rainfall} mm")
print(f"Weather: {weather}")