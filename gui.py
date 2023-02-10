import functions
import PySimpleGUI as sg
import time

sg.theme('Dark')

label_time = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg. InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', button_color='blue')
list_box = sg.Listbox(values=functions.get_todo(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit', button_color='blue')
complete_button = sg.Button('Complete', button_color='blue')
exit_button = sg.Button('Exit', button_color='blue')
text = sg.Text(key='output')

window = sg.Window('My To-Do App',
                   layout=[[label_time],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, text]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("It's %b %d, %y %H:%M:%S"))
    if event == 'Add':
        todo = values['todo'] + '\n'

        todos = functions.get_todo('todos.txt')
        todos.append(todo.title())
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Edit':
        try:
            todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todo()
            index = todos.index(todo)
            todos[index] = new_todo.title()
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        except IndexError:
            sg.popup('Please Select an Item to Edit', font=('Helvetica', 20))

    elif event == 'Complete':
        try:
            todo = values['todos'][0]

            todos = functions.get_todo()
            todos.remove(todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        except IndexError:
            sg.popup('Please Select an Item to Complete', font=('Helvetica', 20))

    elif event == 'Exit':
        exit()

    if event == 'todos':
        window['todo'].update(value=values['todos'][0])

    if event == sg.WIN_CLOSED:
        break

window.close()