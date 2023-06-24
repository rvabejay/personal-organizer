import os.path

events = {}
notes = {}
todo = {}

#load events
def loadEvents():
    #check if file exists
    filetest = os.path.isfile("events.txt")

    #if file exists
    if filetest == True:
        event_file = open("events.txt", "r+")

        for line in event_file:
            data = line [0:-1].split("/")

            date = data[0]
            time = data[1]
            title = data[2]
            description = data[3]
            place = data[4]

            event_data = {}

            event_data["Date"] = date
            event_data["Time"] = time
            event_data["Title"] = title
            event_data["Description"] = description
            event_data["Place"] = place

            events[title] = event_data

        event_file.close()

    #if file does not exist
    else:
        event_file = open("events.txt", "a+")
        event_file.close()


#load notes
def loadNotes():
    #check if file exists
    filetest = os.path.isfile("notes.txt")

    #if file exists
    if filetest == True:
        note_file = open("notes.txt", "r+")

        for line in note_file:
            data = line [0:-1].split("/")

            date = data[0]
            time = data[1]
            title = data[2]
            content = data[3]

            note_data = {}

            note_data["Date"] = date
            note_data["Time"] = time
            note_data["Title"] = title
            note_data["Content"] = content

            notes[title] = note_data

        note_file.close()

    #if file does not exist
    else:
        note_file = open("notes.txt", "a+")
        note_file.close()


#load todo
def loadToDo():
    #check if file exists
    filetest = os.path.isfile("todo.txt")

    #if file exists
    if filetest == True:
        todo_file = open("todo.txt", "r+")

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


#delete events
def removeEvents(input):
    loadEvents()

    temp = {}

    for title in events.keys():
        data = events[title]

        date = data["Date"]
        date = date.replace(" ", "")

        if date == input:
            temp[title] = data

    return temp


#delete notes
def removeNotes(input):
    loadNotes()

    temp = {}

    for title in notes.keys():
        data = notes[title]

        date = data["Date"]
        date = date.replace(" ", "")

        if date == input:
            temp[title] = data

    return temp


#print events
def dateEvents(input, date):
    temp = removeEvents(input)

    #if dictionary is not empty
    if bool(temp) == True:
        print()
        print("Here are all the events that you have for ", date, "\n")
        for title in temp:
            data = temp[title]

            date = data["Date"]
            time = data["Time"]
            description = data["Description"]
            place = data["Place"]

            print(date + "," + time + "\n", title , "\n", description, "\n", place, "\n")

    #if dictionary is empty
    else:
        print()
        print("You do not have any events for this day.")


#print Notes
def dateNotes(input, date):
    temp = removeNotes(input)

    #if dictionary is not empty
    if bool(temp) == True:
        print()
        print("Here are all the notes that you have from", date, "\n")
        for title in temp:
            data = temp[title]

            date = data["Date"]
            time = data["Time"]
            content = data["Content"]

            print(title + "\n", date + "," + time + "\n", content, "\n")

    #if dictionary is empty
    else:
        print()
        print("You do not have any notes from this day.")


#print todo
def dateToDo():
    loadToDo()

    #if dictionary is not empty
    if bool(todo) == True:
        print()
        print("Here are all the tasks that you have.\n")
        for title in todo:
            data = todo[title]

            content = data["Content"]

            print(title, "\n", content, "\n")

    #if dictionary is empty
    else:
        print()
        print("You do not have any unfinished tasks.")


#get date
def overview():
    print("")
    print("sort > Main Menu > My Day")
    print("--- My Day ---")
    while True:
        print()
        date = input("Enter date: ")
        temp = date.replace(" ", "")

        dateEvents(temp, date)
        dateNotes(temp, date)
        dateToDo()
        break
