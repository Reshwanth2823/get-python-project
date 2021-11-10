import math

number = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "its a psquare")
else:
    print(number, "is not a perfect square")
