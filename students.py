students=[]

def student_management():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            semester = input("Enter Semester: ")
            section = input("Enter Section: ")

            duplicate =False

            for student in students:
                if student["id"]==student_id:
                    duplicate=True
                    break
            if duplicate:
                print("Student Id already exists!")
            else:
                student = {
                "id": student_id,
                "name": name,
                "branch": branch,
                "semester": semester,
                "section": section
            }

            students.append(student)

            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("No students found.")
            else:
                print("\n===== STUDENT LIST =====")

                for student in students:
                    print(
                        f"ID: {student['id']} | "
                        f"Name: {student['name']} | "
                        f"Branch: {student['branch']} | "
                        f"Semester: {student['semester']} | "
                        f"Section: {student['section']}"
                    )

        elif choice == "3":
            search_id = input("Enter Student ID to search: ")

            found = False

            for student in students:
                if student["id"] == search_id:
                    print("\nStudent Found!")
                    print("ID:", student["id"])
                    print("Name:", student["name"])
                    print("Branch:", student["branch"])
                    print("Semester:", student["semester"])
                    print("Section:", student["section"])

                    found = True
                    break

            if not found:
                print("Student not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")