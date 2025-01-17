class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder  #public 
        self._type = "Savings" #protected
        self.__balance = balance #private variable

    def get_holder(self):
        return self.holder
    
    def get_type(self):
        return self._type
    
    def get_balance(self):
        return self.__balance
    
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, newBalance: {self.__balance}")
        else:
            print("Deposit Amount must be Positive!")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw Amount: {amount}, RemainingBalance: {self.__balance}")
        else:
            print("Invalid withdrawal Amount!")

account = BankAccount("susruthi", 0)
print("Account Holder: ", account.get_holder())
print("account Type: ", account.get_type())
print("Initial Balance: ", account.get_balance())

account.deposit(1500)
account.withdraw(500)
account.withdraw(2000) 



