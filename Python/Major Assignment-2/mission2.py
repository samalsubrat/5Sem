#using built in functions
def analyzeCities(cleanedCities, previousIntel):
    cleanedSet = set(cleanedCities)
    intelSet = set(previousIntel)
    allCities = cleanedSet.union(intelSet)
    uniqueCities = cleanedSet.symmetric_difference(intelSet)
    highAlert = cleanedSet.intersection(intelSet)
    return allCities, uniqueCities, highAlert

cleanedCities = {"Dnipro", "Kharkiv", "Kyiv", "Lviv", "Odessa"}
previousIntel = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}
allCities, uniqueCities, highAlert = analyzeCities(cleanedCities, previousIntel)
print("All Cities:", allCities)
print("Unique Cities:",uniqueCities)
print("High Alert:",highAlert)

print()

#traditional way
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

cleaned_cities = {"Dnipro", "Kharkiv", "Kyiv", "Lviv", "Odessa"}
previous_intel = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}
all_cities, unique_cities, high_alert = analyze_cities_traditional(cleaned_cities, previous_intel)
print("All cities requiring aid:", all_cities)
print("Unique cities:", unique_cities)
print("High alert cities:", high_alert)

