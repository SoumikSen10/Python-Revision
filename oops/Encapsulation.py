# Modify car class to encapsulate brand attribute , making it private and providing a getter method for it

class Car :
    
    def __init__(self, brand, model) :
        self.__brand = brand
        self.model = model
    
    def get_brand(self) :
        return self.__brand
    
    def set_brand(self,brand) :
        self.__brand = brand
    
    def full_name(self) :
        return f"The car's brand name is : {self.__brand} and model name is : {self.model} ."     
        

car1 = Car("Maruti","Wagon R")   
print(car1.full_name())     

#print(car1.get_brand())

# won't let you access it
#print(car1.brand)

# letting you access
#print(car1.model)

# set brand
car1.set_brand("Safari")

#print(car1.get_brand())

print(car1.full_name())