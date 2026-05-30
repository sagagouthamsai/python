class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance

    def deposit(self,pin,amount):
        if pin!=self.__pin:
            print("Invalid PIN")
            return
        
        elif amount<0:
            print("The amount must be positive")
            return
        
        else :
            self.__balance+=amount

    def withdraw(self,pin,amount):
        if pin!=self.__pin:
            print("Invalid PIN")
            return
        
        elif amount<0:
            print("The amount must be positive")
            return
        
        elif amount>self.__balance:
            print("Insufficient Balance")
            return
                
        else :
            self.__balance-=amount
            print("The withdrawn amount is ",amount)

    def check_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        
        else: 
            print("Invalid PIN")
            return


atm = ATM(1234, 5000)

atm.deposit(1234, 1000)

atm.withdraw(1234, 2000)

print(atm.check_balance(1234))       