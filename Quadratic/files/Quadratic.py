import math
from math import sqrt
a = int(input("Enter the co-eff of x^2: "))
b = int(input("Enter the co-eff of x: "))
c = int(input("Enter the co-eff of constant: "))
d = b*b - 4*a*c
if d >= 0:
    x1 = (-b + sqrt(d))/2
    x2 = (-b - sqrt(d))/2
    print(f"The roots of the equation are:\n Either {x1} OR {x2}")
else:
    print("roots are imaginary!")
print(" ")
name = "Made by Fahad"
print(f"{name:^110}")
input(" ")


