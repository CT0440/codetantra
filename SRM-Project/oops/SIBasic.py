class Parent:
    def fun1(self):
        print("this is fun1 parent class")
    

class Child(Parent):
    def fun2(self):
        print("this is fun2 child class")


obj = Child()
obj.fun1()
obj.fun2()
