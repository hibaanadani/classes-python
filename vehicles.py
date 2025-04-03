vehicles=[]
class Vehicle:
    def __init__(self,brand,model,rentprice,rented):
        self.brand=brand
        self.model=model
        self.rentprice=rentprice
        self.rented=rented

    def __str__(self):
        return f"The car of brand {self.brand} and model {self.model} has rental price of {self.rentprice} and is rented:{self.rented}"
        
    def calculate_rent(self,days):
        return f"Rental price for the vehicle {self.brand} {self.model} for {days} days is {self.rentprice*days}"
    
    def check_rented(self):
        if self.rented==True:
            return f"The vehicle {self.brand} {self.model} is rented"
        else:
            return f"The vehicle {self.brand} {self.model} is not rented"
        
    def rent_vehicle(self):
        if self.rented==False:
            self.rented=True
            return f"The vehicle {self.brand} {self.model} is rented"
        else:
            return f"The vehicle {self.brand} {self.model} is already rented"
        
    def set_rental_price(self,price):
        self.rentprice=price
        return f"New rental price for the vehicle {self.brand} {self.model} is {self.rentprice}"
    
    def get_rental_price(self):
        return f"Rental price for the vehicle {self.brand} {self.model} is {self.rentprice}"
    
    def return_vehicle(self):
        if self.rented==True:
            self.rented=False
            return f"The vehicle {self.brand} {self.model} is returned"
        
class Car(Vehicle):
    def __init__(self, brand, model, rentprice, rented,carseats):
        super().__init__(brand, model, rentprice, rented)
        self.carseats=carseats

    def __str__(self):
        return f"The car of brand {self.brand} and model {self.model} has rental price of {self.rentprice} and is rented:{self.rented} and has {self.carseats} car seats"

class Bike(Vehicle):
    def __init__(self, brand, model, rentprice, rented,motortype):
        super().__init__(brand, model, rentprice, rented)
        self.motortype=motortype
    
    def __str__(self):
        return f"The bike of brand {self.brand} and model {self.model} has rental price of {self.rentprice} and is rented:{self.rented} and has {self.motortype} motor type"
    
class Truck(Vehicle):
    def __init__(self, brand, model, rentprice, rented,maxload):
        super().__init__(brand, model, rentprice, rented)
        self.maxload=maxload
    
    def __str__(self):
        return f"The truck of brand {self.brand} and model {self.model} has rental price of {self.rentprice} and is rented:{self.rented} and has maximum load of {self.maxload} kg"
    
class Bus(Vehicle):
    def __init__(self, brand, model, rentprice, rented,passengers):
        super().__init__(brand, model, rentprice, rented)
        self.passengers=passengers
    
    def __str__(self):
        return f"The bus of brand {self.brand} and model {self.model} has rental price of {self.rentprice} and is rented:{self.rented} and has maximum passengers of {self.passengers}"  

def prompt_user():
    print("1.Add vehicle")
    print("2.Rent vehicle")
    print("3.Return vehicle")
    print("4.Check vehicle")
    print("5.Calculate rent")
    print("6.Set rental price")
    print("7.Get rental price")
    print("8.Exit")
    choice=input("Enter your choice:")
    return choice
    
def add_vehicle():
    add_vehicle=True
    while add_vehicle:
        brand=input("Enter the brand of the vehicle:")
        model=input("Enter the model of the vehicle:")
        rentprice=int(input("Enter the rental price of the vehicle:"))
        rented=input("Is the vehicle rented? (True/False):")
        if rented=="True":
            rented=True
        else:
            rented=False
        print("1.Car")
        print("2.Bike")
        print("3.Truck")
        print("4.Bus")
        choice=input("Enter your choice:")
        if choice=="1":
            carseats=int(input("Enter the number of car seats:"))
            vehicles.append(Car(brand,model,rentprice,rented,carseats))
        elif choice=="2":
            motortype=input("Enter the motor type:")
            vehicles.append(Bike(brand,model,rentprice,rented,motortype))
        elif choice=="3":
            maxload=int(input("Enter the maximum load in kg:"))
            vehicles.append(Truck(brand,model,rentprice,rented,maxload))
        elif choice=="4":
            passengers=int(input("Enter the number of passengers:"))
            vehicles.append(Bus(brand,model,rentprice,rented,passengers))
        print("Vehicle added")
    add_vehicle=input("Do you want to add another vehicle? (Yes/No):")
    if add_vehicle=="Yes":
        add_vehicle()
    else:
        add_vehicle=False

def rent_vehicle():
    for i in range(len(vehicles)):
        print(f"{i+1}.{vehicles[i]}")
    choice=int(input("Enter the number of the vehicle you want to rent:"))
    print(vehicles[choice-1].rent_vehicle())

def return_vehicle():
    for i in range(len(vehicles)):
        print(f"{i+1}.{vehicles[i]}")
    choice=int(input("Enter the number of the vehicle you want to return:"))
    print(vehicles[choice-1].return_vehicle())

def check_vehicle():
    for i in range(len(vehicles)):
        print(f"{i+1}.{vehicles[i]}")
    choice=int(input("Enter the number of the vehicle you want to check:"))
    print(vehicles[choice-1].check_rented())

def calculate_rent():
    for i in range(len(vehicles)):
        print(f"{i+1}.{vehicles[i]}")
    choice=int(input("Enter the number of the vehicle you want to calculate rent for:"))
    days=int(input("Enter the number of days:"))
    print(vehicles[choice-1].calculate_rent(days))

def set_rental_price():
    for i in range(len(vehicles)):
        print(f"{i+1}.{vehicles[i]}")
    choice=int(input("Enter the number of the vehicle you want to set rental price for:"))
    price=int(input("Enter the new rental price:"))
    print(vehicles[choice-1].set_rental_price(price))

def get_rental_price():
    for i in range(len(vehicles)):
        print(f"{i+1}.{vehicles[i]}")
    choice=int(input("Enter the number of the vehicle you want to get rental price for:"))
    print(vehicles[choice-1].get_rental_price())

def main():
    while True:
        choice=prompt_user()
        if choice=="1":
            add_vehicle()
        elif choice=="2":
            rent_vehicle()
        elif choice=="3":
            return_vehicle()
        elif choice=="4":
            check_vehicle()
        elif choice=="5":
            calculate_rent()
        elif choice=="6":
            set_rental_price()
        elif choice=="7":
            get_rental_price()
        elif choice=="8":
            break
        else:
            print("Invalid choice")
