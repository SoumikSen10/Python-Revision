# create two classes battery and engine and let the electriccar class inherit from both, demonstrating multiple inheritance.



class Car :
    
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
    
    def full_name(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} ." 
    

class Battery :
   def battery_info(self) :
       return "This is battery"

class Engine :
    def engine_info(self) :
        return "This is engine"
                
        

class ElectricCarTwo(Battery, Engine, Car) :
    pass  
       

my_tesla = ElectricCarTwo("Tesla","Model S")
print(my_tesla.engine_info())
print(my_tesla.battery_info())

