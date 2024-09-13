import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a todo:" )
input_box = sg.InputText(tooltip='Enter todo', key='todo')
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45,10))

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label],
          [input_box,add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("Todo App", layout=layout, font=('Helvetica', 20))

while True:
    event, values = window.read()

    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except:
                sg.popup("Please select a todo first", font=('Helvetica', 20))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()


