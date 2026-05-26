class Hello:
    def __init__(self, name, age, clg):
        self.name = name #public variavle
        self._age = age #protected variable
        self.__clg = clg #private variable

    def info(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("College:", self.__clg)

    def get_clg(self):
        return self.__clg

h = Hello("Goutham", 19, "JBIET")

h.info()
print(h.name)
print(h.__clg)
print(h.get_clg())

#public variable : can be acessed from anywhere and is visible to any one
#protected variable : can be accessed from anywhere but is not recomended as it is crutial in code 
#private variable : can only be accessed inside the code block but is not visible to anyone
