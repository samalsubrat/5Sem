#using built in functions
def city_intel(high_alert, city_data):
    city_dict = {city: data for data in city_data for city in high_alert if city == data[0]}
    
    total_population = sum(data[1] for data in city_dict.values())
    total_requests = sum(data[2] for data in city_dict.values())
    
    return city_dict, total_population, total_requests

high_alert = {"Kyiv", "Lviv"}
city_data = [("Kyiv", 2800000, 250), ("Kharkiv", 1431000, 180), ("Lviv", 721301, 90), ("Odessa", 1029049, 120)]
high_alert_info, total_population, total_requests = city_intel(high_alert, city_data)
print(high_alert_info, total_population, total_requests)


print()

#using traditional way
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

print("High alert cities info:", high_alert_info)
print("Total population:", total_population)
print("Total requests:", total_requests)
