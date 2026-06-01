class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is coding")

#d = Developer()
#d.work()

class Animal:
    def sound(self):
        print("Animal makes this sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d=Dog()
d.sound()