# from functions import get_todos, write_todos

import functions
import time
current_date = time.strftime("%b %d, %Y. %H:%M:%S")
print("It is", current_date)

while True:
    user_input = input("Enter 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_input.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Not valid. Try edit followed by a todo number")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            print(number)

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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
