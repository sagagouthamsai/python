class student:
    def __init__(self,name):
        self.name=name
        self.__marks=0

    def set_marks(self,name,marks):
        if name==self.name and marks>=0:
            self.__marks=marks
            
            
        elif self.name!=name:
            print("Invalid Name")
            return
        
        elif marks<0:
            print("Marks should be positive")
            return

        else:
            print("Try again")
            return
        
    def get_marks(self):
        return self.__marks
    

s=student("goutham")
s.set_marks("gouth",99)
print(s.get_marks())
