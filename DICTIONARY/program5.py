cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 30000000,
    "Nashik": 2000000
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")