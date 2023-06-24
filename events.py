import os.path

events = {}

def saveEvent(date, time, title, description, place):
    event_file = open("events.txt", "a+")

    event_file.write(date + "/" + time + "/" + title + "/" + description + "/" + place + "\n")

    event_file.close()


def saveChanges():
    event_file = open("events.txt", "w+")

    for title in events:
        data = events[title]

        date = data["Date"]
        time = data["Time"]
        description = data["Description"]
        place = data["Place"]

        event_file.write(date + "/" + time + "/" + title + "/" + description + "/" + place + "\n")

    event_file.close()


def loadEvents():
    #check if file exists
    filetest = os.path.isfile("events.txt")

    #if file exists
    if filetest == True:
        event_file = open("events.txt", "r+")
        events.clear()

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

def schedEvent ():
    loadEvents()
    print("")
    print("Enter event details.")
    while True:
        date = str(input("Date: "))
        time = str(input("Time: "))

        while True:
            title = input("Event title: ")

            if title not in events.keys():
                description = input("Event description: ")
                place = input("Event location: ")

                eventdetails = {}

                eventdetails["Date"] = date
                eventdetails["Time"] = time
                eventdetails["Title"] = title
                eventdetails["Description"] = description
                eventdetails["Place"] = place

                events[title] = eventdetails

                print("\nEvent", title, "is added successfully.")

                saveEvent(date, time, title, description, place)
                break

            else:
                print()
                print("Event title already exists. Please use another event title.")

        break


def seeEvent ():
    loadEvents()
    print("")
    title = input("Enter event title: ")

    if title in events.keys():
        data = events[title]

        date = data["Date"]
        time = data["Time"]
        description = data["Description"]
        place = data["Place"]

        print("Here's the event you are looking for.\n")
        print(date + "," + time + "\n", title , "\n", description, "\n", place)

    else:
        print("Event does not exist.")


def seeAll ():
    loadEvents()

    #if dictionary is not empty
    if bool(events) == True:
        print("")
        print("Here are all the events that you have.\n")
        for title in events:
            data = events[title]

            date = data["Date"]
            time = data["Time"]
            description = data["Description"]
            place = data["Place"]

            print(date + "," + time + "\n", title , "\n", description, "\n", place, "\n")

    #if dictionary is empty
    else:
        print()
        print("You do not have any events. Add a new event in the My Events menu.")

def removeEvent ():
    loadEvents()
    print("")
    title = input("Enter event title: ")

    if title in events.keys():
        del events[title]
        print ("Event", title, "removed successfully.")

    else:
        print("Event does not exist.")

    saveChanges()

def removeAll():
    loadEvents()

    #if dictionary is not empty
    if bool(events) == True:
        print("")
        events.clear()

        print("All events removed successfully.")

        saveChanges()

    #if dictionary is not empty
    else:
        print()
        print("You do not have any events. Add a new event in the My Events menu.")
