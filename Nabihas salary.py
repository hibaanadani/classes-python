income=[]
yearly_expenses={"savings": 0, "rent": 0, "electricity": 0}
salary=float(input("Enter this months salary: "))
while salary != "stop":
    month=input("Enter the month: ")
    salaries={
        "salary":salary,
        "month":month,
    }
    income.append(salaries)
    sum=0
    
    savingspercenatge=float(input("Enter savings percentage: "))
    rentpercenatge= float(input("Enter how much is paid for rent: "))
    electricitypercenatge= float(input("Enter electricity bill: "))
    account ={
        "savings":salary*(savingspercenatge/100),
        "rent":salary*(rentpercenatge/100),
        "electricity":salary*(electricitypercenatge/100),
    }
    yearly_expenses["savings"] += account["savings"]
    yearly_expenses["rent"] += account["rent"]
    yearly_expenses["electricity"] += account["electricity"]
    print(f"{month} expanses are {account['electricity']} for electricity, {account["rent"]} for rent, and {account["savings"]} towards savings")
    sum+=account["savings"]+account["rent"]+account["electricity"]
    amountremained=salary-sum
    print(f"the sum of the expanses for the month {month} is {sum} and {amountremained} is how much remained of the salary")
    salary=input("Enter this months salary: ")