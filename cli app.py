import functions
import time

now = time.strftime("%b %d %Y %H %M %S %p")
print(now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todos = functions.get_todos()

        todo = user_action[4:]
        todos.append(todo + '\n')

        functions.write_todos(todos)

        print(f"Todo {todo} was added to the list.")
    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item.title()}")

    elif user_action.startswith("edit"):
        todos = functions.get_todos()

        number = int(user_action[5:])
        print(f"Editing number {number}")

        new_todo = input("Enter a new todo: ")
        todos[number - 1] = new_todo + '\n'

        functions.write_todos(todos)

    elif user_action.startswith("complete"):
        todos = functions.get_todos()

        number = int(user_action[9:])
        todo_to_remove = todos[number - 1].strip()
        todos.pop(number -1)

        functions.write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list. "
        print(message)

    elif user_action.startswith("exit"):
        break

print("BYE")