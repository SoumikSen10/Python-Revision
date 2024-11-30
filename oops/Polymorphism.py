# define method fuel_type in both car and electriccar classes, but with different behaviours

class Car :
    
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
    
    def full_name(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} ."     
    
    def fuel_type(self) :
        return "Petrol or Diseal"
        

class ElectricCar(Car) :
    
    def __init__(self,brand,model,batterySize) :
        super().__init__(brand,model)
        self.batterySize = batterySize
    
    def info(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} and battery size is : {self.batterySize} ."      
    
    def fuel_type(self) :
        return "Electric charge "
       

tesla = ElectricCar("Tesla","Model S","35 AH")
print(tesla.fuel_type())

maruti = Car("Maruti","WagonR")
print(maruti.fuel_type())
     