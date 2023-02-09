def get_todo(filepath='todos.txt'):

    with open(filepath, 'r') as files:
        todos_local = files.readlines()
    return todos_local


def write_todos(todos_args, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


# will not run in the main.py
if __name__ == "__main__":
    print('hello')