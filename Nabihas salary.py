income = []
yearly_expenses = {"savings": 0, "rent": 0, "electricity": 0}

salary_input = input("Enter this month's salary (or type 'stop' to end): ")

while salary_input!= "stop":
    salary = float(salary_input)
    
    month = input("Enter the month: ")
    salaries = {
        "salary": salary,
        "month": month,
    }
    income.append(salaries)
    
    savings_percentage = float(input("Enter savings percentage: "))
    rent_percentage = float(input("Enter rent percentage: "))
    electricity_percentage = float(input("Enter electricity percentage: "))
    
    savings_amount = salary * (savings_percentage / 100)
    rent_amount = salary * (rent_percentage / 100)
    electricity_amount = salary * (electricity_percentage / 100)
    
    account = {
        "savings": savings_amount,
        "rent": rent_amount,
        "electricity": electricity_amount,
    }
    
    
    yearly_expenses["savings"] += savings_amount
    yearly_expenses["rent"] += rent_amount
    yearly_expenses["electricity"] += electricity_amount
    
    print(f"{month} expenses are {electricity_amount} for electricity, {rent_amount} for rent, and {savings_amount} towards savings.")
    
    total_expenses = savings_amount + rent_amount + electricity_amount
    amount_remaining = salary - total_expenses
    
    print(f"The sum of the expenses for the month {month} is {total_expenses} and {amount_remaining} is the amount remaining from the salary.")
    print(f"The month {month} salary multiplied by 2 for fun is {salary**2}")
    extrasavings=input("Do you want to add extra amount to the savings acount? If yes enter yes ")
    if extrasavings=="yes":
        extrasavingsamount=float(input("Please enter amount that you need to add to the savings account: "))
        savings_amount+=extrasavingsamount
        print(f"You have {savings_amount} for the month {month}")
    salary_input = input("Enter this month's salary (or type 'stop' to end): ")
print(f"Yearly expenses: Savings: {yearly_expenses['savings']}, Rent: {yearly_expenses['rent']}, Electricity: {yearly_expenses['electricity']}")
