# show use of isInstance() to check if my_tesla is an instance of car and electriccar


class Car :
    
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
    
    def full_name(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} ."     
        

class ElectricCar(Car) :
    
    def __init__(self,brand,model,batterySize) :
        super().__init__(brand,model)
        self.batterySize = batterySize
    
    def info(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} and battery size is : {self.batterySize} ."      
       

my_tesla = ElectricCar("Tesla","Model S","35 AH")

     
print(isinstance(my_tesla,Car))  
print(isinstance(my_tesla,ElectricCar))  