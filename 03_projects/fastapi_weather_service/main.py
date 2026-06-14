
from fastapi import FastAPI
import requests
app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Weather Service",
        "endpoints": {
            "about": "/about",
            "weather": "/weather"
        }
    }
@app.get("/about") 
def about(): 
 return { "project": "FastAPI Weather Service", "author": "Anusha" }

import requests

@app.get("/weather")
def weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=14.44"
        "&longitude=79.99"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    response = requests.get(url, timeout=10)

    data = response.json()

    return {
        "city": "Nellore",
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "wind_speed": data["current"]["wind_speed_10m"]
    }