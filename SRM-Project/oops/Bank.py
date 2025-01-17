#Create a class BankAccount with methods for depositing and 
# withdrawing money. Add a method to check the balance and a custom 
# exception to prevent withdrawal if the balance is insufficient

class BankAccount:
    def __init__(self):
        self.balance = 0

    #deposit
    def deposit(self, amount):
        if amount > 0:
           self.balance += amount
           print(f"Deposted: {amount}")

    #withdrawal
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"withdraw:{amount}")
            else:
                print("Insufficient Balance")
        else:
            print("Withdrawal amount must be positive.")

    #checkBalance
    def checkBalance(self):
        try:
            print(f"Current balance: {self.balance}")
        except Exception as e:
            print(f"An error Occured {e}")



account = BankAccount()
print("1. Deposit\n2. WithDraw \n3. checkBalance\n4. Exit")

while True:
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter the amount you want to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the Amount You want to Withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.checkBalance()
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid Input!")





