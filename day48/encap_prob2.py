class bankaccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

        else:
            print("Invalid amount to deposit")
            return
        
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance")
            return
        
        elif amount<0:
            print("Amount must be positive")
            return
        
        else:
            self.__balance-=amount
            print("The withdrawn amount is ",amount)

    def get_balance(self):
        return self.__balance
    
acc = bankaccount()

acc.deposit(5000)
acc.withdraw(2000)

print(acc.get_balance())

print("Test 1")
acc.deposit(1000)
acc.withdraw(500)

print(acc.get_balance())

print("Test 2")
acc.deposit(-100)

print("Test 3")
acc.deposit(1000)
acc.withdraw(5000)
