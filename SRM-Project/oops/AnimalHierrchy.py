class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print(f"dog name is {self.name} says woof!")

class Cat(Animal):
     def sound(self):
        print(f"cat name is {self.name} says meow!")


dog1 = Dog("Jacky")
dog1.sound()
cat1 = Cat("kitty")
cat1.sound()