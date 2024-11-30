# use property decorator in car class to make the model attribute read-only


class Car :
    
    car_count = 0
    
    def __init__(self, brand, model) :
        self.__brand = brand
        self.__model = model
        Car.car_count += 1
        
    def get_brand(self) :
        return self.__brand    
          
    @staticmethod
    def  gen_description() :
        return "Cars are meant for transport"     
    
    @property
    def model(self) :
        return self.__model
        
car1=Car("brand1","model1")
car2=Car("brand2","model2")

print(Car.gen_description())
     
print(car1.get_brand())      


# now we are accessing the method as a property instead of a behaviour    
print(car1.model)          