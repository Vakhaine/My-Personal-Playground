def get_todos(filepath=r'..\todos.txt'):
    """ Reads a text file and
    returns the list of the to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=r'..\todos.txt'):
    """Writes the to-do item list in the text file"""
    with open(r'..\todos.txt', 'w') as file:
        file.writelines(todos_arg)


# print(__name__)
if __name__ in "__main__":
    print("Hello")
    print(get_todos())