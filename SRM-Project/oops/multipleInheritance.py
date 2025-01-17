class Father:
    father_name = "Ravi"
    def __init__(self):
        self.father_name = Father.father_name
        

class Mother:
    mother_name = "Gayathri"
    def __init__(self):
        self.Mother_name = Mother.mother_name

    

class Child(Father, Mother):
    def __init__(self, name):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name

    def info(self):
        print(f"name: {self.name}\nFather's name: {self.father_name} \nMother's name: {self.mother_name}")


obj = Child("sruthi")
obj.info()