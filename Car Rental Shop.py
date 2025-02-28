class Vehical:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.__price=price

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year},Rental Price: {self.__price}")  
    
    def calculate_rental_cost(self,days):
        return days*self.price
    
    def set_rental_price_per_day(self,price):
        self.price=price

    def get_rental_price_per_day(self):
        return self.price
    
class Car(Vehical):
    def __init__(self, brand, model, year, __price, seating_capacity,engine_capacity):
        super().__init__(brand, model, year, __price)
        self.seating_capacity=seating_capacity
        self.engine_capacity=engine_capacity

    def display_info(self):
        print(f"Car: {super().display_info}, seats: {self.seating_capacity}, engine:{self.engine_capacity}")

class Motorcycle(Vehical):
    def __init__(self, brand, model, year, __price, seating_capacity,engine_capacity):
        super().__init__(brand, model, year, __price)
        self.seating_capacity=seating_capacity
        self.engine_capacity=engine_capacity

    def display_info(self):
        print(f"Motorcycle: {super().display_info}, seats: {self.seating_capacity}, engine:{self.engine_capacity}")
     
def show_vehicle_info(vehical):
    return vehical.display_info()