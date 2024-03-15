from app1.Bonus.converter import convert
from parse import parse

feet_inches = input("Enter the feet and inches: ")
# Decoupling functions


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


