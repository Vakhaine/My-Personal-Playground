def liters_to_m3(liters):
    cubic_meters = liters/1000
    return cubic_meters


liters = float(input("Enter liters: "))
result = liters_to_m3(liters)
print(result)