print("\nIf Condition Section")
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")
city = input("Enter a city: ").strip()
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
found = False
for country, cities in countries.items():
    if city in cities:
        print(f"{city} is in {country}")
        found = True
        break
if not found:
    print("City not found in the list.")
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")
country1 = country2 = None
for country, cities in countries.items():
    if city1 in cities:
        country1 = country
    if city2 in cities:
        country2 = country
if country1 and country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country.")
