def isNumber(input):
    no_Space = input.strip()
    if no_Space.isdigit() == True:
        return True
    else:
        return False


def mainmenu ():
    print ("")
    print ("sort – your personal organizer")
    print ("sort > Main Menu")
    print ("")
    print ("[1] My Events")
    print ("[2] My Notes")
    print ("[3] My To-Do List")
    print ("[4] My Day")
    print ("[0] Quit sort")

    while True:
        choice = input("\nSelect an option: ")

        if isNumber(choice) == True:
            return int(choice)
            break

        else:
            print("Input invalid. Enter a number corresponding to an option.")


def eventscheduler ():
    print ("")
    print ("sort > Main Menu > My Events")
    print ("--- My Events ---")
    print ("")
    print ("[1] Schedule an Event")
    print ("[2] See an Event")
    print ("[3] See all Events")
    print ("[4] Remove an Event")
    print ("[5] Remove all Events")
    print ("[0] Return to Main Menu")

    while True:
        choice = input("\nSelect an action: ")

        if isNumber(choice) == True:
            return int(choice)
            break

        else:
            print("Input invalid. Enter a number corresponding to an action.")


def notetaker ():
    print ("")
    print ("sort > Main Menu > My Notes")
    print ("--- My Notes ---")
    print ("")
    print ("[1] Take a Note")
    print ("[2] View a Note")
    print ("[3] View all Notes")
    print ("[4] Delete a Note")
    print ("[5] Delete all Notes")
    print ("[0] Return to Main Menu")

    while True:
        choice = input("\nSelect an action: ")

        if isNumber(choice) == True:
            return int(choice)
            break
            
        else:
            print("Input invalid. Enter a number corresponding to an action.")


def todo ():
    print ("")
    print ("sort > Main Menu > My To-Do List")
    print ("--- My To-Do List ---")
    print ("")
    print ("[1] Add a Task")
    print ("[2] Mark a Task as Done")
    print ("[3] View a Task")
    print ("[4] View all Tasks")
    print ("[0] Return to Main Menu")

    while True:
        choice = input("\nSelect an action: ")

        if isNumber(choice) == True:
            return int(choice)
            break

        else:
            print("Input invalid. Enter a number corresponding to an action.")


def exit():
    print ()
    print ("Thank you for using sort.")
    print ("See you next time!")
    print ()
