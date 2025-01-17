class Animal:
    def speak(self):
        print("Animal Speaks!")

class Mammal(Animal):
    def giveBirth(self):
        print("mammal gives Birth")

class Bird(Animal):
    def layEggs(self):
        print("Birds lay Eggs")
    
class Platpus(Mammal, Bird):
    pass

p = Platpus()
p.speak()
p.giveBirth()
p.layEggs()


        