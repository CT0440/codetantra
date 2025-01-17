class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Polymorphism in action
def animal_sound(animal):
    print(animal.make_sound())

# Create instances of each class
dog = Dog()
cat = Cat()
cow = Cow()

# Call the same method `make_sound` for different objects
animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!
animal_sound(cow)  # Outputs: Moo!
