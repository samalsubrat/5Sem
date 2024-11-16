def days_in_month(month):
    month = month.lower() 
    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        return 31
    elif month == "april" or month == "june" or month == "september" or month == "november":
        return 30
    elif month == "february":
        return "28/29"
    else:
        return "Invalid month"

# Example usage
month_name = input("Enter the month: ")
print("No. of days:", days_in_month(month_name))
