def get_max():
    grades = [9.6, 9.2, 9.7]

    max_grade = max(grades)
    min_grade = min(grades)

    return max_grade, min_grade


max_grade, min_grade = get_max()
print(f"Max: {max_grade}, Min: {min_grade}")
