import functions
import FreeSimpleGUI as gui

lable = gui.Text("Type in a to-do ", text_color= 'white', background_color='black')

input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add", button_color=("white", "black"))

window = gui.Window('My to-Do App', background_color = '#0A97B0', layout=[[lable, input_box, add_button]])
window.read()
window.close()