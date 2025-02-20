income=[]
salary=int(input("Enter this months salary: "))
while salary != "stop":
    month=input("Enter the month: ")
    salaries={
        "salary":salary,
        "month":month,
    }
    income.append(salaries)
    sum=0
    expanses=[]
    savings=int(input("Enter savings percentage: "))
    rent= int(input("Enter how much is paid for rent: "))
    electricity= int(input("Enter electricity bill: "))
    account ={
        "savings":salary*(savings/100),
        "rent":salary*(rent/100),
        "electricity":salary*(electricity/100),
    }
    expanses.append(account)
    print(f"this month expanses are {account['electricity']} for electricity, {account["rent"]} for rent, and {account["savings"]} towards savings")
    sum+=account["savings"]+account["rent"]+account["electricity"]
    salary=input("Enter this months salary: ")