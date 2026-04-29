# Day 9 – String Cleaning Practice

text = "  Chennai, Mumbai, Delhi, chennai , MUMBAI  "

# Step 1: remove extra spaces
text = text.strip()

# Step 2: convert to lower case
text = text.lower()

# Step 3: split into list
cities = text.split(",")

# Step 4: clean each city name
clean_cities = []

for city in cities:
    clean_cities.append(city.strip())

# Step 5: remove duplicates
unique_cities = set(clean_cities)

print("Cleaned unique cities:", unique_cities)