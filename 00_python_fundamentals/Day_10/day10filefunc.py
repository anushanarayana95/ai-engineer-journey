# Day 10 – Functions

def clean_cities(city_list):
    cleaned = []
    for city in city_list:
        cleaned.append(city.strip().lower())
    return set(cleaned)


cities = [" Chennai ", "Mumbai", "delhi ", "CHENNAI"]

result = clean_cities(cities)
print("Cleaned unique cities:", result)