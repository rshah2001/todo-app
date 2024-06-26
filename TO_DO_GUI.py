import functions
import FreeSimpleGUI as sg

# this creates a label on the window
label = sg.Text("Type in a to-do")

# creating an input box
input_box = sg.InputText(tooltip= "Enter a Todo")

# adding a button
add_button = sg.Button("Add")

# This will be the title of the window.
# this layout expects a list. Items placed inside the inner brackets will be placed in one row
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
'''put the input box in next line; put both of them in separate [] '''

window.read()  # this displays the window on the screen
window.close()
