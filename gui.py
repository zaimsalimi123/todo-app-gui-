import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
button = sg.Button("Add")

window = sg.Window("Todo App", layout=[[label],
                                            [input_box], [button]],
                                    font=("Helvatica",20))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()