import math

# Solve a quadratic equation using the quadratic formula. Use relational 
# and arithmetic operators to check if the roots are real or imaginary based 
# on the discriminant

def solve_Quadratic(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if (D > 0):
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)

        return f"Two distnict roots are: {root1: .2f} & {root2: .2f}"

    elif (D == 0):
        root = -b / (2 * a)
        return f"One real root {root: .2f}"

    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-D) / (2 * a)

        return f"imaginary roots: {real_part: .2f} ± {imaginary_part: .2f}i"



a = float(input("Enter coefficient of a: "))
b = float(input("Enter coefficient of b: "))
c = float(input("Enter coefficient of c: "))

result = solve_Quadratic(a, b, c)
print(result)

