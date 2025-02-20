income=[]
salary=float(input("Enter this months salary: "))
while salary != "stop":
    month=input("Enter the month: ")
    salaries={
        "salary":salary,
        "month":month,
    }
    income.append(salaries)
    sum=0
    expanses=[]
    savings=float(input("Enter savings percentage: "))
    rent= float(input("Enter how much is paid for rent: "))
    electricity= float(input("Enter electricity bill: "))
    account ={
        "savings":salary*(savings/100),
        "rent":salary*(rent/100),
        "electricity":salary*(electricity/100),
    }
    expanses.append(account)
    print(f"this month expanses are {account['electricity']} for electricity, {account["rent"]} for rent, and {account["savings"]} towards savings")
    sum+=account["savings"]+account["rent"]+account["electricity"]
    amountremained=salary-sum
    print(f"the sum of the expanses are {sum} and {amountremained} is how much remained of the salary")
    salary=input("Enter this months salary: ")