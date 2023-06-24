import menu
import events
import notes
import todolist
import myday
import importlib


#main menu loop
while True:
    main_option = menu.mainmenu()

    if main_option == 1:
        while True:
            event_option = menu.eventscheduler()

            if event_option == 1:
                events.schedEvent()

            elif event_option == 2:
                events.seeEvent()

            elif event_option == 3:
                events.seeAll()

            elif event_option == 4:
                events.removeEvent()

            elif event_option == 5:
                events.removeAll()

            elif event_option == 0:
                break

            else:
                print("Input invalid. Enter a valid number corresponding to an action.")

    elif main_option == 2:
        while True:
            note_option = menu.notetaker()

            if note_option == 1:
                notes.takeNote()

            elif note_option == 2:
                notes.viewNote()

            elif note_option == 3:
                notes.viewAll()

            elif note_option == 4:
                notes.deleteNote()

            elif note_option == 5:
                notes.deleteAll()

            elif note_option == 0:
                break

            else:
                print("Invalid input. Enter a valid number corresponding to an action.")

    elif main_option == 3:
        while True:
            todo_option = menu.todo()

            if todo_option == 1:
                todolist.addTask()

            elif todo_option == 2:
                todolist.markDone()

            elif todo_option == 3:
                todolist.viewTask()

            elif todo_option == 4:
                todolist.viewAll()

            elif todo_option == 0:
                break

            else:
                print("Invalid input. Enter a valid number corresponding to an action.")

    elif main_option == 4:
        importlib.reload(myday)
        import myday
        myday.overview()

    elif main_option == 0:
        menu.exit()
        break

    else:
        print("Input invalid. Enter a valid number corresponding to an option.")
