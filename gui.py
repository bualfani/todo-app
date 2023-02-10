import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg. InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todo(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(values)
    if event == 'Add':
        todo = values['todo'] + '\n'

        todos = functions.get_todo('todos.txt')
        todos.append(todo.title())
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Edit':
        todo = values['todos'][0]
        new_todo = values['todo']

        todos = functions.get_todo()
        index = todos.index(todo)
        todos[index] = new_todo.title()
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Complete':
        todo = values['todos'][0]

        todos = functions.get_todo()
        todos.remove(todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')

    elif event == 'Exit':
        exit()

    if event == 'todos':
        window['todo'].update(value=values['todos'][0])

    if event == sg.WIN_CLOSED:
        break

window.close()