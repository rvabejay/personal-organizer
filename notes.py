import os.path

notes = {}

def saveNote (date, time , title, content):
    note_file = open("notes.txt", "a+")

    note_file.write(date + "/" + time + "/" + title + "/" + content + "\n")

    note_file.close()


def saveChanges():
    note_file = open("notes.txt", "w+")

    for title in notes:
        data = notes[title]

        date = data["Date"]
        time = data["Time"]
        content = data["Content"]

        note_file.write(date + "/" + time + "/" + title + "/" + content + "\n")

    note_file.close()

def loadNotes():
    #check if file exists
    filetest = os.path.isfile("notes.txt")

    #if file exists
    if filetest == True:
        note_file = open("notes.txt", "r+")
        notes.clear()

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


def takeNote():
    loadNotes()
    print("")
    print("Enter note details.")
    while True:
        date = str(input("Date: "))
        time = str(input("Time: "))

        while True:
            title = input("Note title: ")

            if title not in notes.keys():
                content = input("Enter note contents: ")

                notedetails = {}

                notedetails["Date"] = date
                notedetails["Time"] = time
                notedetails["Title"] = title
                notedetails["Content"] = content

                notes[title] = notedetails

                print("\nNote", title, "is added successfully.")

                saveNote(date, time, title, content)
                break

            else:
                print()
                print("Note title already exists. Please use another note title.")

        break


def viewNote():
    loadNotes()
    print("")
    title = input("Enter note title: ")

    if title in notes.keys():
        data = notes[title]

        date = data["Date"]
        time = data["Time"]
        content = data["Content"]

        print("Here's the note you are looking for.\n")
        print(title + "\n", date + "," + time + "\n", content)

    else:
        print("Note does not exist.")


def viewAll():
    loadNotes()

    #if dictionary is not empty
    if bool(notes) == True:
        print("")
        print("Here are all the notes that you have.\n")
        for title in notes:
            data = notes[title]

            date = data["Date"]
            time = data["Time"]
            content = data["Content"]

            print(title + "\n", date + "," + time + "\n", content, "\n")

    #if dictionary is empty
    else:
        print()
        print("You do not have any notes. Add a new note on the My Notes menu.")

def deleteNote():
    loadNotes()
    print("")
    title = input("Enter note title: ")

    if title in notes.keys():
        del notes[title]
        print("Note", title, "deleted successfully.")

    else:
        print("Note does not exist.")

    saveChanges()

def deleteAll():
    loadNotes()

    #if dictionary is not empty
    if bool(notes) == True:
        print("")
        notes.clear()

        print("All notes deleted successfully.")

        saveChanges()

    #if dictionary is not empty
    else:
        print()
        print("You do not have any notes. Add a new note on the My Notes menu.")
