def get_nr_items(names):
    items = names.split(",")
    count = len(items)
    return count


result = get_nr_items("john, lisa, teresa")
print(result)

