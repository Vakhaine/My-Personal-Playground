def get_average():
    with open("../files/data.txt")as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_sum = sum(values) / len(values)
    return average_sum


average = get_average()
print(average)