def temp(temperature):
    if temperature > 25:
        return "Hot"
    if 15 <= temperature >= 25:
        return "Warm"
    else:
        return "Cold"


result = temp(35)
print(result)