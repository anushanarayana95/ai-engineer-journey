# Day 5 – Lists

cities = ["Chennai", "Mumbai", "Delhi"]

print("Original list:", cities)

cities.append("Bangalore")
print("After append:", cities)

cities.remove("Delhi")
print("After remove:", cities)

print("\nLooping through list:")
for city in cities:
   print(city)