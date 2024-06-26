import functions
import FreeSimpleGUI as Sg

# this creates a label on the window
label = Sg.Text("Type in a to-do")

# creating an input box
input_box = Sg.InputText(tooltip="Enter a Todo", key="todo")

# adding a button
add_button = Sg.Button("Add")

# This will be the title of the window.
# this layout expects a list. Items placed inside the inner brackets will be placed in one row
window = Sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
'''put the input box in next line; put both of them in separate [] '''

# using a while loop so it keeps the window open
while True:
    # Event will read the button and value will display the text written in it
    event, values = window.read()  # this displays the window on the screen
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            # the values below will print a dictionary
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)  # this will have the new todo from the new_todo and the add button
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break


window.close()
