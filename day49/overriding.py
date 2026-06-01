class Person:

    def introduce(self):
        print("I am a person")


class Student(Person):

    def introduce(self):
        print("I am a student")


s = Student()

s.introduce()