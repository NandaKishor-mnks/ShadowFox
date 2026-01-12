# Program 1: BMI Category Finder
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
else:
    print("Underweight")

# Program 2: City to Country Identifier
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found in the list")

# Program 3: Check if two cities belong to the same country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
else:
    print("They don't belong to the same country")
