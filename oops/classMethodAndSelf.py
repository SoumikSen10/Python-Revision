# Add a method to the car class that displays the full name of the car (brand and model)

class Car :
    
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
    
    def full_name(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} ."     
        

car1 = Car("Maruti","Wagon R")   
print(car1.full_name())     