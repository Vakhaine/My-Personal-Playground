def get_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    return age


result = get_age(1990, 2024)
print(result)