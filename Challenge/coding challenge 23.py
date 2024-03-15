def get_max():
    grades = [9.6, 9.2, 9.7, 10]

    max_value = [float(i) for i in grades]
    return max(max_value)


maximum = get_max()
print(maximum)

