# Create a Car class with attributes like brand and model. Then create an instance of this class

class Car :
   def __init__(self , brand, model) : 
    self.brand = brand
    self.model = model


my_car = Car("Maruti","Wagon R")

print("Brand - ", my_car.brand ,"\n" "Model - ", my_car.model)


my_new_car = Car("Tata","Safari")

print("Brand - ", my_new_car.brand ,"\n" "Model - ", my_new_car.model)