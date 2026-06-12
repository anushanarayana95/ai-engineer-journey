import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=14.44"
    "&longitude=79.99"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)
response = requests.get(url)

print(response.status_code)

print(response.json())

import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=14.44"
    "&longitude=79.99"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)
response = requests.get(url, timeout=10)



data = response.json()

temperature = data["current"]["temperature_2m"]

print("Temperature:", temperature)

time = data["current"]["time"]

print("Time:", time)




temperature = data["current"]["temperature_2m"]

humidity = data["current"]["relative_humidity_2m"]

wind_speed = data["current"]["wind_speed_10m"]

time = data["current"]["time"]
#Simple Weather Report
print("\nWeather Report")
print("----------------")

print("Location: Nellore")
print("Time:", time)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Wind Speed:", wind_speed, "km/h")

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Success")
    else:
        print("API Error:", response.status_code)

except Exception as e:

    print("Something went wrong:", e)
report = f"""
# Weather Report

Location: Nellore

Time: {time}

Temperature: {temperature} °C

Humidity: {humidity} %

Wind Speed: {wind_speed} km/h
"""

with open("/workspaces/ai-engineer-journey/03_projects/weather_api_analyzer/weather_report.md", "w") as f:
    f.write(report)
city = "Nellore"

print("Location:", city)