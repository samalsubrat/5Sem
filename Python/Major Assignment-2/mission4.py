def track_supplies(supplies):
    supply_dict = {}
    for city, supply, quantity in supplies:
        if city not in supply_dict:
            supply_dict[city] = {}
        supply_dict[city][supply] = quantity
    return supply_dict

supplies = [("Kyiv", "Food", 500), ("Moscow", "Medicines", 200), ("Lviv", "Water", 300), 
            ("Saint Petersburg", "Blankets", 100), ("Kharkiv", "Food", 150)]
supply_distribution = track_supplies(supplies)
print("Supply Distribution:",supply_distribution)
