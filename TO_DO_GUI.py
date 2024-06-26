import functions
import FreeSimpleGUI as Sg

# this creates a label on the window
label = Sg.Text("Type in a to-do")

# List box; functions.get_todos will get all the list of existing todos from the todo.txt file
list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

# creating an input boxx
input_box = Sg.InputText(tooltip="Enter a Todo", key="todo")

# adding a button
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")


# This will be the title of the window.
# this layout expects a list. Items placed inside the inner brackets will be placed in one row
window = Sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
'''put the input box in next line; put both of them in separate [] '''

# using a while loop so it keeps the window open
while True:
    # Event will read the button and value will display the text written in it
    event, values = window.read()  # this displays the window on the screen


    # just for testing
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            # the values below will print a dictionary
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)  # this will have the new todo from the new_todo and the add button
            functions.write_todos(todos)

            # we point to the list box instance and the we point to the method update and the values = todos(updated)
            window['todos'].update(values=todos)  # updates in real time

        case "Edit":
            todo_to_edit = values['todos'][0]

            # getting new todo from the user. This is because it is inside the values dictionary and key is 'todo'
            new_todo = values['todo']
            todos = functions.get_todos()  # getting current todos from the function

            # this will help to replace the existing todo with a new todo
            index = todos.index(todo_to_edit)  # Getting the index of the todo to edit and storing it a variable
            todos[index] = new_todo  # now with the index from the previous line it will be replaced with the new todo
            functions.write_todos(todos)  # we write the new todo to the existing list to the write todo function

            ''' window is a function used above and what we are doing is that we are using the key value from List_box
            and it will give us the list box instance. window is like the mother of all and
            we use .update method of listbox '''

            window['todos'].update(values=todos)  # Updating the list at the same time

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break


window.close()
