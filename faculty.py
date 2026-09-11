faculty = []


def faculty_management():
    while True:
        print("\n===== FACULTY MANAGEMENT =====")
        print("1. Add Faculty")
        print("2. View Faculty")
        print("3. Search Faculty")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            faculty_id = input("Enter Faculty ID: ")
            name = input("Enter Faculty Name: ")
            department = input("Enter Department: ")
            subject = input("Enter Subject: ")

            duplicate = False

            for teacher in faculty:
                if teacher["id"] == faculty_id:
                    duplicate = True
                    break

            if duplicate:
             print("Faculty ID already exists!")

            else:
                teacher = {
                "id": faculty_id,
                "name": name,
                "department": department,
                "subject": subject
                }

                faculty.append(teacher)

                print("Faculty added successfully!")

        elif choice == "2":
            if not faculty:
                print("No faculty found.")
            else:
                print("\n===== FACULTY LIST =====")

                for teacher in faculty:
                    print(
                        f"ID: {teacher['id']} | "
                        f"Name: {teacher['name']} | "
                        f"Department: {teacher['department']} | "
                        f"Subject: {teacher['subject']}"
                    )

        elif choice == "3":
            search_id = input("Enter Faculty ID to search: ")

            found = False

            for teacher in faculty:
                if teacher["id"] == search_id:
                    print("\nFaculty Found!")
                    print("ID:", teacher["id"])
                    print("Name:", teacher["name"])
                    print("Department:", teacher["department"])
                    print("Subject:", teacher["subject"])

                    found = True
                    break

            if not found:
                print("Faculty not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")