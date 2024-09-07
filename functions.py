def get_todos(filepath="todo.csv.txt"):
    """Get the existing todo.csv from the file.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filepath="todo.csv.txt"):
    """Write the Entered todo.csv in the file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

