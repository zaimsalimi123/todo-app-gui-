import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)

st.title("My Todo App")
st.subheader("This app is to improve your productivity.")
st.write("This is my todo app")

for todo in todos:
    st.checkbox(todo.title())

st.text_input(label="Enter todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')