from classMethodAndSelf import Car

# Inheritance
class ElectricCar(Car) :
    
    def __init__(self,brand,model,batterySize) :
        super().__init__(brand,model)
        self.batterySize = batterySize
    
    def info(self) :
        return f"The car's brand name is : {self.brand} and model name is : {self.model} and battery size is : {self.batterySize} ."         

car2 = ElectricCar("Maruti","WagonR","35 AH")

print(car2.info())        