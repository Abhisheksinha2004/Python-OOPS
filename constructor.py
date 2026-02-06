#Without constructor
# class Car:
#     def set_details(self,brand,color):
#         self.brand=brand
#         self.color=color
        
# car1=Car()
# car1.set_details("Tesla","Red")

# print(car1.brand)
# print(car1.color) 

#with constructor
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
      
         
car1=Car("Tesla","Red")
print(car1.brand,car1.color)         