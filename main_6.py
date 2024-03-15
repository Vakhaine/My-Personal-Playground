def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(r'..\todos.txt', 'w') as file:
        file.writelines(todos_arg)


while True:
    user_input = input("Enter 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = get_todos(r'..\todos.txt')

        todos.append(todo + '\n')

        write_todos(filepath=r'..\todos.txt', todos_arg=todos)

    elif user_input.startswith('show'):

        todos = get_todos(r'..\todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            print(number)
            number = number - 1

            todos = get_todos(r'..\todos.txt')

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(r'..\todos.txt', todos)

        except ValueError:
            print("Not valid. Try edit followed by a todo number")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            print(number)

            todos = get_todos(r'..\todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(r'..\todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list successfully!."
            print(message)
        except IndexError:
            print("You are out of range. Try again!")
            continue
        except ValueError:
            print("Not valid. Try complete followed by a todo number")
            continue

    elif user_input.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("Bye!")
