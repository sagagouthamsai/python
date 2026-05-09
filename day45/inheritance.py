class employee():
    def __init__(self,name,role,pay):
        self.name=name
        self.role=role
        self.pay=pay
class info(employee):
    def show(self):
        print(self.name,self.role,self.pay)

emp1=info('goutham','data analyst','50000')
emp1.show()

print(emp1.name)