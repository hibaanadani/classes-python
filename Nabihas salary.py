salaries=[]
salary=input("Enter this months salary: ")
month=input("Enter the month: ")
savings=input("Enter savings percentage: ")
rent= input("Enter how much is paid for rent:")
electricity= input("Enter electricity bill: ")

while salary != "stop":
    salaries={
        "salary":salary,
        "month":month,
    }
    account ={
        "savings":salary*(savings/100),
        "rent":salary*(rent/100),
        "electricity":salary*(electricity/100),
    }