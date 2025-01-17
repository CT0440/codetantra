class BankExample:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            print(f"deposited: {amount}")


    def withdraw(self, amount):
        if amount > 0:
            if (amount <= self.balance):
                print(f"Withdrawal Amount: {amount}")
                self.balance -= amount

            
            else:
                print("Insuffiecient balance")
            
       
    def checkbalance(self):
        print("current balance: {self.balance}")
    
    def exit(self):
        print("Exit")
        
    

account = BankExample()
print("1. Deposit\n 2. Withdraw \n 3. CheckBalance\n 4. Exit")

while(True):
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        amount = float(input("Enter the amount you want to deposit: "))
        account.deposit(amount)
    elif (choice == 2):
         amount = float(input("Enter the amount you want to withdraw: "))
         account.withdraw(amount)
    elif (choice == 3):
        account.checkbalance()
    elif(choice == 4):
        account.exit()
    else:
        print("Invalid choice")



