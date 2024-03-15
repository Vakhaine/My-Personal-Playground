# To Calculate the free fall time of an object
# t = time, h = free fall distance, g = gravity (9.80665 m/s2)

def calculate_time(h, g=9.80665):
    # g = 9.80665
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)



