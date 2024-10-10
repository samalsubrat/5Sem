room_type = input("Enter room type (Standard/Deluxe/Suite): ").lower()
nights = int(input("Enter number of nights: "))
season = input("Enter season (peak/off): ").lower()

if room_type == "standard":
    price_per_night = 100
elif room_type == "deluxe":
    price_per_night = 150
elif room_type == "suite":
    price_per_night = 250
else:
    print("Invalid room type")
    exit()

total_cost = price_per_night * nights

if nights > 3:
    total_cost *= 0.9
if season == "off":
    total_cost *= 0.85

print(f"Total cost: ${total_cost:.2f}")
