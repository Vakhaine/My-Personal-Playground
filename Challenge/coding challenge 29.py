def strength(password):
    special_char = "!@#$%^&*()_-+=<>?"
    if (len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password)
            and any(char in special_char for char in password)):
        return "Strong Password"
    elif (len(password) >= 8 and any(char.isdigit() for char in password)
          and any(char.isupper() for char in password)):
        return "Moderate Password"
    else:
        return "Weak Password"


user_password = input("Enter a strong password: ")
print(strength(user_password))
