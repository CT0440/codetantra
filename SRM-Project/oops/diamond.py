class Class1:
    def showclass(self):
        print("class1")

class Class2(Class1):
    def showclass(self):
        print("class2")

class Class3(Class1):
    def showclass(self):
        print("class3")

class Class4(Class2, Class3):
    def showclass(self):
       print("class4")

obj = Class4()
obj.showclass()
Class2.showclass(obj)
Class3.showclass(obj)
Class1.showclass(obj)