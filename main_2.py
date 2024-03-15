user_choice = "Enter 'add', 'show', 'edit', 'complete' or 'exit': "

while True:
    user_input = input(user_choice)
    user_input = user_input.strip()

    match user_input:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open(r'..\todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open(r'..\todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open(r'..\todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item.capitalize()}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open(r'..\todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            with open(r'..\todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open(r'..\todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open(r'..\todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
print("Bye!")