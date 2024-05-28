students_info = {}


def add_student(name, age, grade, subjects, students):
    if name not in students:
        students[name] = {"age": age, "grade": grade, "subjects": subjects}
        print(f"Student {name} added successfully.")
    else:
        print(f"Student {name} already exists. Please enter a new student name to add.")
        print("If you  want to update a student, please choose 2 from the main menu.")


def update_student(name, students):

    if name not in students:
        print(f"Student {name} doesn't exist. You can add a new student from the main menu.")
    else:
        new_name = input("Enter updated name or use 0 to keep the current name.")
        new_age = int(input("Enter updated age or use 0 to keep the current age."))
        new_grade = float(input("Enter updated grade or use 0 to keep the current grade."))
        new_subjects = input("Enter updated subjects list (comma-separated) \
        or use 0 to keep the current subjects.").split(",")
        # May include option for adding/deleting a subject from the list

        if new_name != "0":
            print(f"Name of {name} updated to {new_name}.")
            students[new_name] = students[name]
            del students[name]
            name = new_name
        else:
            print(f"Name of {name} was not updated.")

        if new_age != 0:
            print(f"Age of {name} updated from {students[name]['age']} to {new_age}.")
            students[name]["age"] = new_age
        else:
            print(f"Age of {name} was not updated.")

        if new_grade != 0:
            print(f"Grade of {name} updated from {students[name]['grade']} to {new_grade}.")
            students[name]["grade"] = new_grade
        else:
            print(f"Grade of {name} was not updated.")

        if new_subjects != ["0"]:
            print(f"Subjects of {name} updated from {students[name]['subjects']} to {new_subjects}.")
            students[name]["subjects"] = new_subjects
        else:
            print(f"Subjects of {name} were not updated.")


def delete_student(name, students):
    if name not in students:
        print(f"Student {name} doesn't exist!")
    else:
        print(f"Student {name} deleted successfully.")
        del students[name]


def search_student(name, students):
    if name not in students:
        print(f"Student {name} doesn't exist!")
    else:
        print(f"{name}'s record:")
        print(f" - Age: {students[name]['age']}")
        print(f" - Grade: {students[name]['grade']}")
        print(f" - Subjects: {', '.join(students[name]['subjects'])}")


def list_all_students(students):
    if not students:
        print("Currently there are no records.")
    else:
        counter = 1
        for student, info in students.items():
            print(f"{counter}. {student}")
            print(f" - Age: {info['age']}")
            print(f" - Grade: {info['grade']}")
            print(f" - Subjects: {', '.join(info['subjects'])}")
            print()
            counter += 1


def main():

    while True:

        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student's name: ")  # may update with a specific name format
            student_age = int(input("Enter student's age with digits: "))
            student_grade = float(input("Enter student's grade with digits: "))
            student_subjects = input("Enter student's subjects (comma-separated): ").split(',')

            # This check to be updated with Regex at a later point depending on the name format:
            for letter in student_name:
                if not (letter.isalpha() or letter.isspace()):
                    print("Invalid name, use only letters and spaces!")
            else:
                add_student(student_name, student_age, student_grade, student_subjects, students_info)

        elif choice == '2':
            student_name = input("Enter student's name to update: ")
            update_student(student_name, students_info)

        elif choice == '3':
            student_name = input("Enter student's name to delete: ")
            delete_student(student_name, students_info)

        elif choice == '4':
            student_name = input("Enter student's name to search: ")
            search_student(student_name, students_info)

        elif choice == '5':
            list_all_students(students_info)

        elif choice == '6':
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
