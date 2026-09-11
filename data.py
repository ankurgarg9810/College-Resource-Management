import json

from students import students
from faculty import faculty
from rooms import rooms
from schedule import schedules


def save_data():
    data = {
        "students": students,
        "faculty": faculty,
        "rooms": rooms,
        "schedules": schedules
    }

    with open("college_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")


def load_data():
    global students, faculty, rooms, schedules

    try:
        with open("college_data.json", "r") as file:
            data = json.load(file)

            students.clear()
            students.extend(data.get("students", []))

            faculty.clear()
            faculty.extend(data.get("faculty", []))

            rooms.clear()
            rooms.extend(data.get("rooms", []))

            schedules.clear()
            schedules.extend(data.get("schedules", []))

    except FileNotFoundError:
        print("No previous data found. Starting fresh.")