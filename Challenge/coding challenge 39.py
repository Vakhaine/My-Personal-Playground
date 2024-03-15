def get_str(string):
    if len(string) < 8:
        return False
    else:
        return True


result = get_str("mylongpassword")
print(result)