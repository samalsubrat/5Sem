from datetime import datetime, timedelta

def new_date_and_day(start_date, days):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    new_date = start + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d"), new_date.strftime("%A")

# Example usage
print(new_date_and_day("2024-08-27", 5))  # Output: ("2024-09-01", "Sunday")
