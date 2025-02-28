vehicles=[]
class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.__price=price

    def display_info(self):
        return f"{self.brand} {self.model},Year: {self.year},Rental Price: ${self.__price}/day"
    
    def calculate_rental_cost(self,days):
        return f"Rental cost for {self.brand} {self.model} for {days} days: ${days*self.__price}"
    
    def set_rental_price_per_day(self,price):
        self.__price=price

    def get_rental_price_per_day(self):
        return self.__price
    
class Car(Vehicle):
    def __init__(self, brand, model, year, price, seating_capacity):
        super().__init__(brand, model, year,price)
        self.seating_capacity=seating_capacity

    def display_info(self):
        return f"Car:{super().display_info()}, seats: {self.seating_capacity}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, price,engine_capacity):
        super().__init__(brand, model, year, price)
        self.engine_capacity=engine_capacity

    def display_info(self):
        return f"Motorcycle:{super().display_info()},engine:{self.engine_capacity}"
     

def prompt():
    print("Choose from the options below:")
    print("1.Add vehicle")
    print("2.Display Vehicles available")
    print("3.Display vehicle info")
    print("4.Rent the vehicle chosen for x days:")
    print("5.Set rental price per day:")
    print("6.Exit the program")
    option=int(input("Enter the option chosen"))
    
    return option

def addVehicle():
    type_of_vehicle=input("Is the vehicle added a car or a motorcycle: ")
    if type_of_vehicle=="car":
        brand=input("Enter the brand of the car: ")
        model=input("Enter the model of the car: ")
        year=int(input("Enter the year of the car: "))
        rental_price_per_day =input("Enter the rental price per day of the car: ")
        number_of_seats=int(input("Enter how many seats does the car have:" ))
        newcar=Car(brand,model,year,rental_price_per_day,number_of_seats)
        vehicles.append(newcar)

    elif type_of_vehicle=="motorcycle":
        brand=input("Enter the brand of the motorcycle: ")
        model=input("Enter the model of the motorcycle: ")
        year=int(input("Enter the year of the motorcycle: "))
        rental_price_per_day =input("Enter the rental price per day of the motorcycle: ")
        engine_capacity=int(input("Enter the capacity of the engine:" ))
        newmotorcycle=Motorcycle(brand,model,year,rental_price_per_day,engine_capacity)
        vehicles.append(newmotorcycle)

def display_vehicles_available():
    print(*enumerate(vehicles),sep='\n')

def show_vehicle_info(vehicle):
    print (vehicle.display_info())

def rent_for_x_days():
    chosen_vehicle=input("Enter the number of the vehicle choosen: ")
    numb_of_days=int(input("Enter the numbers of days you want to rent the chosen vehicle for: "))   


toyota = Car("Toyota","Corolla",2020,50,5)
yamaha = Motorcycle("Yamaha","R1",2019,30,"998cc")
show_vehicle_info(toyota)
show_vehicle_info(yamaha)

print(toyota.calculate_rental_cost(3))
print(yamaha.calculate_rental_cost(5))

toyota.set_rental_price_per_day(55)
show_vehicle_info(toyota)
