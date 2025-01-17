class Father:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__savings = 50000 #private
   
    def showSavings(self):
       return self.__savings 

class Child(Father):
    def __init__(self, name, salary, pocket_money):
        super().__init__(name, salary)
        self.pocket_money = pocket_money
        
    def showDetails(self):
        print(f"Father's name: {self.name}")
        print(f"father's Salry: {self.salary}")
        print(f"pocketmoney: {self.pocket_money}")
        

    def getSavings(self):
        print(f"saving's of father {self.showSavings()}")


father = Father("Ravi", 25000)
child = Child("Ravi", 25000, 250)

child.showDetails()
father.showSavings()
child.getSavings()

