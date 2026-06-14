# FastAPI Weather Service

## Project Overview

This project is a simple FastAPI application that provides weather information through API endpoints.

It demonstrates:

* FastAPI basics
* API endpoints
* JSON responses
* HTTP requests
* External API integration
* Live weather data retrieval

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Requests
* Open-Meteo API

---

## Project Structure

```text
fastapi_weather_service/
│
├── main.py
└── README.md
```

---

## Endpoints

### Home Endpoint

```text
/
```

Returns a welcome message.

Example:

```json
{
  "message": "Hello FastAPI"
}
```

---

### About Endpoint

```text
/about
```

Returns project information.

Example:

```json
{
  "project": "FastAPI Weather Service",
  "author": "Anusha"
}
```

---

### Weather Endpoint

```text
/weather
```

Fetches live weather data from Open-Meteo API.

Example Response:

```json
{
  "city": "Nellore",
  "temperature": 37.9,
  "humidity": 35,
  "wind_speed": 1.1
}
```

Values change based on current weather conditions.

---

## Installation

Install required packages:

```bash
pip install fastapi uvicorn requests
```

---

## Run the Application

Navigate to project folder:

```bash
cd 03_projects/fastapi_weather_service
```

Start server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

---

## Testing Endpoints

Home:

```bash
curl http://127.0.0.1:8001/
```

About:

```bash
curl http://127.0.0.1:8001/about
```

Weather:

```bash
curl http://127.0.0.1:8001/weather
```

---

## What I Learned

### FastAPI

* Creating FastAPI applications
* Defining API endpoints
* Returning JSON responses
* Running applications with Uvicorn

### APIs

* Sending HTTP requests
* Receiving JSON data
* Extracting nested values
* Working with external services

### Backend Development

* Client → API → Response workflow
* REST API fundamentals
* Endpoint design

---

## Key Concepts

```text
Client
   ↓
FastAPI Endpoint
   ↓
Python Function
   ↓
External API
   ↓
JSON Response
```

---

## Future Improvements

* Add weather forecast endpoint
* Add city search functionality
* Add error handling
* Add HTML homepage
* Deploy application online

---

## Author

Anusha Narayana
