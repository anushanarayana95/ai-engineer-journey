# Weather API Analyzer

## Project Overview

This project fetches live weather data from the Open-Meteo API using Python.

The application sends an HTTP request, receives weather information in JSON format, extracts useful fields, and generates a weather report.

---

## Technologies Used

* Python
* Requests
* JSON
* REST API
* Git
* GitHub

---

## Features

* Fetch current weather data
* Read JSON responses
* Extract weather information
* Generate weather reports
* Handle API errors using try/except

---

## Weather Information Collected

* Temperature
* Humidity
* Wind Speed
* Time

---

## Skills Demonstrated

### API Requests

```python
requests.get()
```

### JSON Parsing

```python
response.json()
```

### Nested Dictionary Access

```python
data["current"]["temperature_2m"]
```

### Error Handling

```python
try:
    ...
except:
    ...
```

### File Handling

```python
with open(...)
```

---

## Project Structure

weather_api_analyzer/

* weather_analyzer.py
* weather_report.md
* README.md

---

## Lessons Learned

* How APIs work
* HTTP requests and responses
* Status codes
* JSON data structures
* Error handling
* Report generation

---

## Future Improvements

* User-selected city
* Weather forecasts
* Multiple cities
* Save data to CSV
* Build a dashboard using Streamlit
