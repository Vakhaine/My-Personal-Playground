def get_maximum():
    celsius_value = [14, 15.1, 12.3]
    maximum = max(celsius_value)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)