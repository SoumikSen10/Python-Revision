# Add a class variable to car that keeps track of the number of cars created


class Car :
    
    car_count = 0
    
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
        Car.car_count += 1
    
    def full_name(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} ."     
    
    def fuel_type(self) :
        return "Petrol or Diseal"
        
       

Car("Maruti","WagonR")
Car("brand2","model2")

print(Car.car_count)
     