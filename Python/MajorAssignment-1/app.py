#Code by Subrat Samal  |  Reg no: 2241019269  |  Section: 19

#Question 1: Basic Salary

def basic_salary(hourly_rate,hours_per_week):
    regular_hours = min(hours_per_week, 40)
    monthly_salary = hourly_rate * regular_hours * 4
    return monthly_salary

def overtime_salary(hourly_rate,hours_per_week):
    if hours_per_week <= 40:
        return 0
    
    overtime_hours = hours_per_week - 40
    overtime_rate = hourly_rate * 1.5
    monthly_overtime = overtime_hours * overtime_rate * 4
    return monthly_overtime

def total_salary(hourly_rate, hours_per_week):
    base = basic_salary(hourly_rate, hours_per_week)
    overtime = overtime_salary(hourly_rate, hours_per_week)
    return base + overtime


#Question 2: Tax Calculation

def tax_amount(salary):
    if salary < 60000:
        return salary * 0.10
    elif salary <= 85000:
        return salary * 0.15
    else:
        return salary * 0.20
    

#Question 3: Gross Salary Calculation

def gross_salary(basic_salary_amount):
    allowances = basic_salary_amount * 0.20  
    tax = tax_amount(basic_salary_amount)
    return basic_salary_amount + allowances - tax


# Question 4: Salary bracket categorization

def salary_bracket(gross_salary_amount):
    if gross_salary_amount < 50000:
        return "Low income"
    elif gross_salary_amount <= 80000:
        return "Middle income"
    else:
        return "High income"
    

# Question 5: Employee report generation
def employee_report(names, hourly_rates, hours_worked):
    print("\nEMPLOYEE SALARY REPORT")
    print("-" * 70)
    print(f"{'Name':<15} {'Basic Salary':>12} {'Gross Salary':>12} {'Tax Amount':>12} {'Bracket':>15}")
    print("-" * 70)
    
    for name, rate, hours in zip(names, hourly_rates, hours_worked):
        basic = total_salary(rate, hours)
        tax = tax_amount(basic)
        gross = gross_salary(basic)
        bracket = salary_bracket(gross)
        
        print(f"{name:<15} {basic:>12.2f} {gross:>12.2f} {tax:>12.2f} {bracket:>15}")
    
    print("-" * 70)
    
    
employee_names = ["Shashwat Sahoo", "Bikash Mallick", "Saswat Sharma"]
hourly_rates = [400, 500, 600]
hours_per_week = [45, 40, 50]

employee_report(employee_names, hourly_rates, hours_per_week)