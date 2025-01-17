class Dog:
    breed = "Jerman Shepherd" #class attribute
    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute
    def sound(self):
        return f"Woofing!"

dog1 = Dog("Jacky", 11)
print(dog1.name, dog1.age)#jacky 11
print(dog1.breed)
print(dog1.sound())
