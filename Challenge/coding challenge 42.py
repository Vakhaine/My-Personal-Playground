def water_state(temperature):
    freezing_point = 0
    boiling_point = 100

    if temperature <= freezing_point:
        return "Solid"
    elif freezing_point < temperature < boiling_point:
        return "Liquid"
    else:
        return "Gas"


result = water_state(123)
print(result)