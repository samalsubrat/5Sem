def clean_and_sort_list(cities):
    cleaned_list = []
    for city in cities:
        if city not in cleaned_list:
            cleaned_list.append(city)
    for i in range(len(cleaned_list)):
        for j in range(len(cleaned_list) - i - 1):
            if cleaned_list[j] > cleaned_list[j + 1]:
                cleaned_list[j], cleaned_list[j + 1] = cleaned_list[j + 1], cleaned_list[j]
    return cleaned_list

def analyze_cities_traditional(cleaned_cities, previous_intel):
    cleaned_list = list(cleaned_cities)
    intel_list = list(previous_intel)
    
    all_cities = cleaned_list.copy()
    for city in intel_list:
        if city not in all_cities:
            all_cities.append(city)
    
    unique_cities = []
    for city in all_cities:
        if (city in cleaned_list and city not in intel_list) or (city in intel_list and city not in cleaned_list):
            unique_cities.append(city)
    
    high_alert = []
    for city in cleaned_list:
        if city in intel_list:
            high_alert.append(city)
    
    return set(all_cities), set(unique_cities), set(high_alert)

def city_intel_traditional(high_alert, city_data):
    city_dict = {}
    for city in high_alert:
        for data in city_data:
            if data[0] == city:
                city_dict[city] = data
    
    total_population = 0
    total_requests = 0
    for city, data in city_dict.items():
        total_population += data[1]
        total_requests += data[2]
    
    return city_dict, total_population, total_requests

def track_supplies_traditional(supplies):
    supply_dict = {}
    for city, supply, quantity in supplies:
        if city not in supply_dict:
            supply_dict[city] = {}
        supply_dict[city][supply] = quantity
    return supply_dict

# Main Program
cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
previous_intel = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}
city_data = [("Kyiv", 2800000, 250), ("Kharkiv", 1431000, 180), ("Lviv", 721301, 90), ("Odessa", 1029049, 120)]
supplies = [("Kyiv", "Food", 500), ("Moscow", "Medicines", 200), ("Lviv", "Water", 300), 
            ("Saint Petersburg", "Blankets", 100), ("Kharkiv", "Food", 150)]

cleaned_cities = clean_and_sort_list(cities)
all_cities, unique_cities, high_alert = analyze_cities_traditional(cleaned_cities, previous_intel)
high_alert_info, total_population, total_requests = city_intel_traditional(high_alert, city_data)
supply_distribution = track_supplies_traditional(supplies)

print("Cleaned cities:", cleaned_cities)
print("All cities requiring aid:", all_cities)
print("Unique cities:", unique_cities)
print("High alert cities:", high_alert)
print("High alert cities info:", high_alert_info)
print("Total population:", total_population)
print("Total requests:", total_requests)
print("Supply distribution:", supply_distribution)
