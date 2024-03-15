
user_choice = "Enter 'add', 'show', 'edit', 'complete' or 'exit': "
# todos = []

while True:
    user_input = input(user_choice)
    user_input = user_input.strip()

    match user_input:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open(r'..\todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(r'..\todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            file = open(r'..\todos.txt', 'r')
            todos = file.readlines()
            file.close()

            #print(todos) prints items in todos with line break charactor

            #using a for loop:
            #new_todos = []

            #for item in todos:
            #   new_item = item.strip('\n') #to remove the line break char
            #   new_todos.append(new_item)

            #using a list comprehension:
            #new_todos = [item.strip('\n') for item in todos]

            #for index, item in enumerate(new_todos):#changed from todos to new_todos
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item.capitalize()}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number -1)
        case 'exit':
            break
print("Bye!")