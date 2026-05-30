class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show_details(self):
        print(f"Name : {self.name}\nAge : {self.age}")

class Student(Person):
    def __init__(self, name, age,course="CSE"):
        super().__init__(name,age)
        self.course=course

    def show_course(self):
        print("Course : ",self.course)

s = Student("Goutham", 19)

s.show_details()
s.show_course()