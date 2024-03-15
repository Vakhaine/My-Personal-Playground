while True:
    user_input = input("Enter 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_input = user_input.strip()

    if 'add' in user_input:
        todo = user_input[4:]

        with open(r'..\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open(r'..\todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_input:

        with open(r'..\todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif 'edit' in user_input:
        number = int(user_input[5:])
        print(number)
        number = number - 1

        with open(r'..\todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + '\n'

        with open(r'..\todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_input:
        number = int(user_input[9:])
        print(number)

        with open(r'..\todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open(r'..\todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif 'exit' in user_input:
        break
    else:
        print("Command is not valid!")
print("Bye!")