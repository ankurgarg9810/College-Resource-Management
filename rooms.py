from schedule import schedules
from faculty import faculty
import json
rooms = []





def room_allocation():
    print("\n===== AUTOMATIC ROOM ALLOCATION =====")

    section = input("Enter Class/Section: ")
    student_count = int(input("Enter Number of Students: "))

    suitable_rooms = []

    for room in rooms:
        if room["status"] == "Available" and room["capacity"] >= student_count:
            suitable_rooms.append(room)

    if suitable_rooms:
        best_room = min(suitable_rooms, key=lambda room: room["capacity"])

        best_room["status"] = "Occupied"

        print("\nRoom Allocated Successfully!")
        print("Class:", section)
        print("Students:", student_count)
        print("Room:", best_room["room_number"])
        print("Block:", best_room["block"])
        print("Capacity:", best_room["capacity"])

    else:
        print("\nNo suitable room available.")
def room_management():
    while True:
        print("\n===== ROOM MANAGEMENT =====")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Search Room")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            room_number = input("Enter Room Number: ")
            block = input("Enter Block: ")
            capacity = int(input("Enter Room Capacity: "))
            duplicate = False

            for room in rooms:
                if room["room_number"] == room_number:
                    duplicate = True
                    break

            if duplicate:
                print("Room Number already exists!")

            else:
                room = {
                "room_number": room_number,
                "block": block,
                "capacity": capacity,
                "status": "Available"
            }

            rooms.append(room)
            print("Room added successfully!")

        elif choice == "2":
            if not rooms:
                print("No rooms found.")
            else:
                print("\n===== ROOM LIST =====")

                for room in rooms:
                    print(
                        f"Room: {room['room_number']} | "
                        f"Block: {room['block']} | "
                        f"Capacity: {room['capacity']} | "
                        f"Status: {room['status']}"
                    )

        elif choice == "3":
            search_room = input("Enter Room Number to search: ")

            found = False

            for room in rooms:
                if room["room_number"] == search_room:
                    print("\nRoom Found!")
                    print("Room:", room["room_number"])
                    print("Block:", room["block"])
                    print("Capacity:", room["capacity"])
                    print("Status:", room["status"])

                    found = True
                    break

            if not found:
                print("Room not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

def class_allocation():
    print("\n===== CLASS ALLOCATION =====")

    section = input("Enter Class/Section: ")
    student_count = int(input("Enter Number of Students: "))
    subject = input("Enter Subject: ")
    faculty_name = input("Enter Faculty Name: ")
    time = input("Enter Time: ")

    # Check faculty
    faculty_exists = False

    for teacher in faculty:
        if teacher["name"].lower() == faculty_name.lower():
            faculty_exists = True
            break

    if not faculty_exists:
        print("\nFaculty not found.")
        print("Please add the faculty first.")
        return

    # Find suitable rooms
    suitable_rooms = []

    for room in rooms:

        if room["status"] != "Available":
            continue

        if room["capacity"] < student_count:
            continue

        # Check room conflict
        room_conflict = False

        for schedule in schedules:
            if schedule["room"] == room["room_number"] and schedule["time"] == time:
                room_conflict = True
                break

        if not room_conflict:
            suitable_rooms.append(room)

    # Check if a room is available
    if not suitable_rooms:
        print("\nNo suitable room available.")
        return

    # Select smallest suitable room
    best_room = min(
        suitable_rooms,
        key=lambda room: room["capacity"]
    )

    # Allocate room
    best_room["status"] = "Occupied"

    # Create schedule
    schedule = {
        "section": section,
        "subject": subject,
        "faculty": faculty_name,
        "room": best_room["room_number"],
        "time": time
    }

    schedules.append(schedule)

    print("\n===== ALLOCATION SUCCESSFUL =====")
    print("Class:", section)
    print("Students:", student_count)
    print("Subject:", subject)
    print("Faculty:", faculty_name)
    print("Room:", best_room["room_number"])
    print("Block:", best_room["block"])
    print("Capacity:", best_room["capacity"])
    print("Time:", time)