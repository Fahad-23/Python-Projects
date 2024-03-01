from addition import sum
from subtract import sub
from mult import mult
from division import div
try:
    op = input("Which Arithmetic operation would you like to perform(add, sub, div, mult): ").lower()
    a = int(input("Enter first number: "))
    b = int(input("Enter the second number: "))

    if op == "sub" or op == "subtract":
        print(sum(a, b))
    elif op == "add" or op == "addition" :
        print(sub(a, b))
    elif op == "mult" or op == "multiply":
        print(mult(a, b))
    elif op == "div" or op == "divide" or op == "division":
        print(div(a, b))

except ValueError:
    print("Enter a number!")

print(" ")
name = "Made by Fahad"
print(f"{name:^110}")
input("Press any key! ")



