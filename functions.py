FilEPATH = "todos.txt"


def get_todos(filepath=FilEPATH):  # this is variable used to call the function below in the add function inside the()
    # similar to filepath = 'todos.txt'
    with open(filepath, 'r') as file_local:   # while using the "with" function you don't need to close the file.
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FilEPATH):  # filepath and todos_org are called parameters
    with open(filepath, 'w') as file:  # same as above
        file.writelines(todos_arg)
    # no return function as it is a process


if __name__ == "__main__":
    print("Hello")
