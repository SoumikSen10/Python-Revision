# add static method to car class that returns general description of a car

"""
static method belongs to class rather than to an instance of a class

"""

class Car :
    
    car_count = 0
    
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
        Car.car_count += 1
          
    @staticmethod
    def  gen_description() :
        return "Cars are meant for transport"     
        
car1=Car("brand1","model1")
car2=Car("brand2","model2")

print(Car.gen_description())
     