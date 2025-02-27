class Vehical:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price

    def display_info(self):
        print(f"The car is {self.brand} {self.model}, Year: {self.year},Rental Price: {self.price}")  
    
    def calculate_rental_cost(self,days):
        return days*self.price
    
    def set_rental_price_per_day(self,price):
        self.price=price

    def get_rental_price(self):
        return self.price
    



    
    
    

    