class carRental:
    def __init__(self,brand,model,year,price,seating):
        self.brand=''
        self.model=''
        self.year=0
        self.price=0
        self.seating=0

    def display_info(self):
        print(f"The car is {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating}, Rental Price: {self.price}")  
    def calculate_rental_cost(self,days):
        if days>=1:
            rental_cost=days*self.price
        return rental_cost
    
    def additional_attribute(self):
        print(f"The car {self.model} has {self.seating}")


def prompt():
    print("Select from the options below: ")
    print("1. Display vehicle details")
    print("2. Display Rental costs")
    print("1. Display vehicle details")

    
    
    

    