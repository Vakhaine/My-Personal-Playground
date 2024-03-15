def get_temp(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"


result = get_temp(7)
print(result)