feet_inches = input("Enter the feet and inches: ")
def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    if inches > 12:
        return None
    meters = feet * 0.3048 + inches * 0.0254
    return meters



result = convert(feet_inches)

if result is None:
    print("Enter a valid input")
elif result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


