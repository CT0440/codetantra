class Reactangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
class Square(Reactangle):
    def __init__(self, side):
        super().__init__(side, side)


class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
        self.height = side

    def volume(self):
        return  self.area() * self.height


obj = Cube(4)
obj.area()
print(f"area of square : {obj.area()}")
print(f"volume of cube : {obj.volume()}")
