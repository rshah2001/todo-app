import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To Do App")
st.subheader("This is my todo app")
st.write("this app is to increase your productivity ")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new Todo...")
