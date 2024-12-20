import functions
import FreeSimpleGUI as gui

lable = gui.Text("Type in a to-do ")

input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")
window = gui.Window('My to-Do App', layout=[[lable, input_box, add_button]])
window.read()
window.close()