def get_max():
    grades = [9.6, 9.2, 9.7, 12, 10.2]

    float_values = [float(i) for i in grades]
    return float_values


values = get_max()
print(f"Max: {max(values)}, Min: {min(values)}")

