# A bank wants to calculate compound interest for a given principal, rate, 
# and time. Implement the formula using arithmetic and comparison 
# operators to determine if the calculated interest is above a specified 
# amount.
P = float(input("Enter PrincipleAmount:"))
T = int(input("Enter Years:"))
R = float(input("Enter Rate of Interest:"))

A = P * (1 + (R / 100))**T

CI = A - P
print(f"The Compound Interst is: {CI: .2f}")
print(f"The Amount is: {A: .2f}")
