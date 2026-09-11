from students import students, student_management

from faculty import faculty, faculty_management

from rooms import rooms, room_management, room_allocation, class_allocation
from schedule import schedules, schedule_management
from data import save_data, load_data

def main():
    while True:
        print("\n===== COLLEGE RESOURCE MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Faculty Management")
        print("3. Room Management")
        print("4. Room Allocation")
        print("5. View Schedule")
        print("6. Automatic Class Allocation")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            
            student_management()

        elif choice == "2":
            faculty_management()

        elif choice == "3":
            room_management()

        elif choice == "4":
           room_allocation()

        elif choice == "5":
            schedule_management()

        elif choice == "6":
             class_allocation()

        elif choice == "7":
         save_data()
         print("Thank you for using the system!")
         break

        else:
            print("Invalid choice. Please try again.")

load_data()
main()