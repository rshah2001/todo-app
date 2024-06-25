# importing it from function.py this is done so that the code doesn't get long
# Syntax from "name of the file" "import what you want to import"
# from functions import get_todos, write_todos
# we just use import function in this case as its difficult to define all functions one by one
# instead what we do is we use "functions." followed by the function call  dirrectly where we need to use it
import functions
import time


now = time.strftime("Hi it is %b %d,%Y. \nTime is %H:%M")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # strip function removes the extra spaces from the input taken by the user

# string which will check only the first 4-5 characters
    if user_action.startswith("add"):   # or function will let you type either add or new to the code
        # list slicing: that we are extracting all the characters of the string starting at index 4
        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines() read previous todos added in txt and next line wll append i.e add more below it
        # file.close()
        todos = functions.get_todos() # 'todos.txt is the argument value to the parameter in the function above

        todos.append(todo+ '\n')
        # adding them to the list

        # file = open('todos.txt', 'w')
        # file.writelines(todos) overide the todos.txt file everytime you run the program with new todos
        # file.close()

        # with open('todos.txt', 'w') as file:  #same as above
        #   file.writelines(todos)
        # same as below
        functions.write_todos(todos)



    elif user_action.startswith("show"):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos]  #this is a neater way to write i.e list comprehession

        for index, item in enumerate(todos):
            item = item.strip('\n')  # this strip removes the \n from every line before showing us the result
            row = f"{index + 1}. {item}" # index = index + 1 this is same as row = f"{index+1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            # number = int(input("Number of the todo to edit: "))
            number = int(user_action[5:] ) # this will take input from the user in the same line as they type edit
            number = number - 1

            todos = functions.get_todos()  # custom function created above
            new_todo= input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        # will not give the red error below if the user eneters a string infact it will give a value error in red
        # to remove that and have a better user experience it will print invalid command and ask the user to enter again
        except ValueError:
            print("Your command is not valid!. ")
            continue  # this command will break and go back to the first line of while code.
            # which is same as
            # user_action = input("Type add, show, edit, complete or exit: ")
            # user_action = user_action.strip()

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            # number = number - 1 same as todos.pop(number-1)
            # todos.pop(number - 1)

            todos = functions.get_todos()
            index = number -1
            todo_to_be_removed = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"{todo_to_be_removed} was removed from the list."
            print(message)
        except IndexError:
            print("Enter a number within range.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid.")
print("Bye")