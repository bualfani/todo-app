import functions
import time

print(time.strftime("It's %b %d, %y %H:%M:%S"))

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todo('todos.txt')

        todos.append(todo.title())

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todo()

        for index, item in enumerate(todos):
            print(f'{index+1}.', item.strip('\n'))
        print(f"You have {len(todos)} items in your list")

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todo()

            number = int(user_action[5:])
            number -= 1
            new_todo = input("New To Do: ") + '\n'
            todos[number] = new_todo.capitalize()

            functions.write_todos(todos)

        except ValueError:
            print("Please Enter a Number ")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todo()

            complete = int(user_action[9:])
            complete -= 1
            todo_to_remove = todos[complete].strip('\n')
            todos.pop(complete)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list")

        except IndexError:
            print("Invalid Entry, Please Try Again")
            continue

        except ValueError:
            print("Please Enter a Number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not valid")
