import functions

import FreeSimpleGUI as sg

label = sg.Text("Enter a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")


window = sg.Window("Todo_app", layout=[[label], [input_box,add_button]])

window.read()
window.close()

