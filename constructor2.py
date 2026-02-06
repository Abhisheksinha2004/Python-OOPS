class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
student1=Student("Rakesh",100,"A+")
student2=Student("Kalpesh",50,"B+")

print(student1.name,student1.age,student1.grade) 
print(student2.name,student2.age,student2.grade)       