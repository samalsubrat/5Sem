#using built in functions
def clean_and_sort_list(cities):
    return sorted(set(cities))

def analyze_cities_modern(cleaned_cities, previous_intel):
    all_cities = cleaned_cities | previous_intel
    unique_cities = cleaned_cities ^ previous_intel
    high_alert = cleaned_cities & previous_intel
    return all_cities, unique_cities, high_alert

def city_intel_modern(high_alert, city_data):
    city_dict = {city: data for city in high_alert for data in city_data if data[0] == city}
    total_population = sum(data[1] for data in city_dict.values())
    total_requests = sum(data[2] for data in city_dict.values())
    return city_dict, total_population, total_requests

def track_supplies_modern(supplies):
    supply_dict = {}
    for city, supply, quantity in supplies:
        supply_dict.setdefault(city, {}).update({supply: quantity})
    return supply_dict

# Main Program
cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
previous_intel = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}
city_data = [("Kyiv", 2800000, 250), ("Kharkiv", 1431000, 180), ("Lviv", 721301, 90), ("Odessa", 1029049, 120)]
supplies = [("Kyiv", "Food", 500), ("Moscow", "Medicines", 200), ("Lviv", "Water", 300), 
            ("Saint Petersburg", "Blankets", 100), ("Kharkiv", "Food", 150)]

cleaned_cities = set(clean_and_sort_list(cities))
all_cities, unique_cities, high_alert = analyze_cities_modern(cleaned_cities, previous_intel)
high_alert_info, total_population, total_requests = city_intel_modern(high_alert, city_data)
supply_distribution = track_supplies_modern(supplies)

print("Cleaned cities:", sorted(cleaned_cities))
print("All cities requiring aid:", all_cities)
print("Unique cities:", unique_cities)
print("High alert cities:", high_alert)
print("High alert cities info:", high_alert_info)
print("Total population:", total_population)
print("Total requests:", total_requests)
print("Supply distribution:", supply_distribution)
