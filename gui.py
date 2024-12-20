from traceback import print_tb

import functions
import FreeSimpleGUI as gui

lable = gui.Text("Type in a to-do ", text_color= 'white', background_color='black')

input_box = gui.InputText(tooltip="Enter todo", key ="todo")
add_button = gui.Button("Add", button_color=("white", "black"))
layout = [[lable, input_box, add_button]]
window = gui.Window('My to-Do App', background_color = '#0A97B0', layout= layout, font=('helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos('todos.tx')
            new_todo = values['todo'] +" \n"
            todos.append(new_todo)
            functions.write_todos('todos.tx', todos)
        case gui.WIN_CLOSED:
            break
window.close()