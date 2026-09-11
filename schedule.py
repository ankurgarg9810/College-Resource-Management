schedules = []


def schedule_management():
    while True:
        print("\n===== SCHEDULE MANAGEMENT =====")
        print("1. Add Schedule")
        print("2. View Schedule")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            section = input("Enter Class/Section: ")
            subject = input("Enter Subject: ")
            faculty_name = input("Enter Faculty Name: ")
            room_number = input("Enter Room Number: ")
            time = input("Enter Time: ")

            conflict = False

            for schedule in schedules:
                if schedule["room"] == room_number and schedule["time"] == time:
                    conflict = True
                    break

            if conflict:
                print("\nConflict detected!")
                print("This room is already scheduled at this time.")

            else:
                schedule = {
                    "section": section,
                    "subject": subject,
                    "faculty": faculty_name,
                    "room": room_number,
                    "time": time
                }

                schedules.append(schedule)

                print("\nSchedule added successfully!")

        elif choice == "2":
            if not schedules:
                print("No schedules found.")

            else:
                print("\n===== CLASS SCHEDULE =====")

                for schedule in schedules:
                    print(
                        f"Class: {schedule['section']} | "
                        f"Subject: {schedule['subject']} | "
                        f"Faculty: {schedule['faculty']} | "
                        f"Room: {schedule['room']} | "
                        f"Time: {schedule['time']}"
                    )

        elif choice == "3":
            break

        else:
            print("Invalid choice.")