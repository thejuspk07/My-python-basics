#From a list of city names, print only the cities that start with "B" using startswith().
cities = [
    "Bengaluru",
    "Delhi",
    "Bhopal",
    "Mumbai",
    "Berlin",
    "Chennai",
    "Boston",
    "Kochi",
    "Barcelona",
    "Pune"
]
for i in cities:
    if i.startswith("B"):
        print(i)
