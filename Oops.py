# class Car():
#     #method
#     def start(self):
#         print("CAR IS STARTING....")
        
#     def stop(self):
#         print("CAR IS STOPPING...")
        
        
# car1=Car()
# car2=Car()

# car1.start()
# car1.stop()

# car2.start() 
# car2.stop()  

class Car:
    def set_details(self,brand,color):
        self.brand=brand
        self.color=color
        
    def show_details(self):
        print(f"This car is a {self.color} {self.brand}")
        
car1=Car()
car1.set_details("Tesla","Red")

car2=Car()
car2.set_details("BMW","Blue") 
car1.show_details()
car2.show_details()                 

class student:
    def set_details(self,name,marks):
        self.name=name
        self.marks=marks
        
student1=student()
student1.set_details("Abhishek",98)
print(student1.name,student1.marks)        