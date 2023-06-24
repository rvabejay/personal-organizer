import os.path

todo = {}

def saveToDo(title, content):
    todo_file = open("todo.txt", "a+")

    todo_file.write(title + "/" + content + "\n")

    todo_file.close()


def saveChanges():
    todo_file = open("todo.txt", "w+")

    for title in todo:
        data = todo[title]

        content = data["Content"]

        todo_file.write(title + "/" + content + "\n")

    todo_file.close()


def loadToDo():
    #check if file exists
    filetest = os.path.isfile("todo.txt")

    #if file exists
    if filetest == True:
        todo_file = open("todo.txt", "r+")
        todo.clear()

        for line in todo_file:
            data = line [0:-1].split("/")

            title = data[0]
            content = data[1]

            task_data = {}

            task_data["Title"] = title
            task_data["Content"] = content

            todo[title] = task_data

        todo_file.close()

    #if file does not exist
    else:
        todo_file = open("todo.txt", "a+")
        todo_file.close()

def addTask():
    loadToDo()
    print("")
    print("Enter task details.")
    while True:
        title = input("Task title: ")

        if title not in todo.keys():
            content = input("Task description: ")

            taskdetails = {}

            taskdetails["Title"] = title
            taskdetails["Content"] = content

            todo[title] = taskdetails

            print("\nTask", title, "is added successfully.")

            saveToDo(title, content)
            break

        else:
            print()
            print("Task title already exists. Please use another task title.")


def markDone():
    loadToDo()
    print("")
    title = input("Enter task title: ")

    if title in todo.keys():
        del todo[title]
        print ("Task", title, "is marked as completed.")

    else:
        print("Task does not exist.")

    saveChanges()


def viewTask():
    loadToDo()
    print("")
    title = input("Enter task title: ")

    if title in todo.keys():
        data = todo[title]

        content = data["Content"]

        print("Here's the task you are looking for.\n")
        print(title, "\n", content)

    else:
        print("Task does not exist.")


def viewAll():
    loadToDo()

    #if dictionary is not empty
    if bool(todo) == True:
        print("")
        print("Here are all the tasks that you have.\n")
        for title in todo:
            data = todo[title]

            content = data["Content"]

            print(title, "\n", content, "\n")

    #if dictionary is empty
    else:
        print()
        print("You do not have any tasks. Add a new task on the My To-Do List menu.")
