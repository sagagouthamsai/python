class Hello:
    def __init__(self, name, age, clg):
        self.name = name
        self._age = age
        self.__clg = clg

    def info(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("College:", self.__clg)

    def get_clg(self):
        return self.__clg

h = Hello("Goutham", 19, "JBIET")

h.info()
print(h.name)
print(h.get_clg())
print(h.__clg)