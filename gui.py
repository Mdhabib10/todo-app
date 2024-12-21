

import functions
import FreeSimpleGUI as gui


lable = gui.Text("Type in a to-do ", text_color= 'white', background_color='black')

input_box = gui.InputText(tooltip="Enter todo", key ="user_inputKey")

add_button = gui.Button("Add", button_color=("white", "black"))

list_box = gui.Listbox(values = functions.get_todos('todos.tx'), key ='list_items', enable_events=True, size=(45,10), font=('Helvetica', 20), background_color="#CDF5FD")
edit_button = gui.Button("Edit", button_color=("white", "black"))

layout = [[lable, input_box, add_button],[list_box, edit_button]]

window = gui.Window('My to-Do App', background_color = '#0A97B0', layout= layout, font=('helvetica', 20))

while(True):
    event, values  = window.read()
    print(1, event)
    print(2, values)
    print(3, values['list_items'])
    match event:
        case "Add":
            todos = functions.get_todos('todos.tx')
            new_todo = values['user_inputKey'] + "\n"
            todos.append(new_todo)
            functions.write_todos('todos.tx', todos)
            window['list_items'].update(values=todos)
        case "Edit":
            user_selection = values['list_items'][0]
            new_edit = values['user_inputKey'] +"\n"

            todos = functions.get_todos('todos.tx')
            index = todos.index(user_selection)
            todos[index] = new_edit
            functions.write_todos('todos.tx', todos)
            window['list_items'].update(values=todos)
        case 'list_items':
            window['user_inputKey'].update(value = values['list_items'][0])

        case gui.WIN_CLOSED:
            break

window.close()