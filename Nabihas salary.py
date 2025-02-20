income=[]
salary=input("Enter this months salary: ")
sum=0
while salary != "stop":
    month=input("Enter the month: ")
    salaries={
        "salary":salary,
        "month":month,
    }
    income.append(salaries)
    savings=input("Enter savings percentage: ")
    rent= input("Enter how much is paid for rent: ")
    electricity= input("Enter electricity bill: ")
    account ={
        "savings":salary*(savings/100),
        "rent":salary*(rent/100),
        "electricity":salary*(electricity/100),
    }
    sum+=account["savings"]+account["rent"]+account["electricity"]
    salary=input("Enter this months salary: ")