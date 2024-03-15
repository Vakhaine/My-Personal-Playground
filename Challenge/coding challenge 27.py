def circle_area(r):
    pi = 3.14
    area = 2*pi * r**2
    return area


r = float(input("Enter the radius of the circle: "))
result = (circle_area(r))
print(result)

