class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.__price=price

    def display_info(self):
        return f"{self.brand} {self.model}, Year: {self.year},Rental Price: {self.__price}"
    
    def calculate_rental_cost(self,days):
        return days*self.price
    
    def set_rental_price_per_day(self,price):
        self.__price=price

    def get_rental_price_per_day(self):
        return self.__price
    
class Car(Vehicle):
    def __init__(self, brand, model, year, __price, seating_capacity):
        super().__init__(brand, model, year, __price)
        self.seating_capacity=seating_capacity

    def display_info(self):
        return f"Car: {super().display_info}, seats: {self.seating_capacity}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, __price,engine_capacity):
        super().__init__(brand, model, year, __price)
        self.engine_capacity=engine_capacity

    def display_info(self):
        return f"Motorcycle: {super().display_info},engine:{self.engine_capacity}"
     
def show_vehicle_info(vehicle):
    return vehicle.display_info()

toyota = Car("Toyota","Corolla",2020,50,5)
toyota.display_info()