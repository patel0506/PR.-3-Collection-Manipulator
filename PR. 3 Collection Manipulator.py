print("Welcome to the Student Data Organizer!")

student_list = []
student_dict = {}
student_subject = set()

while True:
    print("Select an option:")
    print("1. Add a student")
    print("2. Display all students")
    print("3. Update a student information")
    print("4. Delete a student")
    print("5. Display Subjects offered")
    print("6. Exit")
    n = int(input("Enter your choice: "))

    match n:
        case 1:
            print("Enter Student Details:")
            student_id = int(input("Enter student ID: "))
            student_name = input("Enter student name: ")
            student_age = int(input("Enter student age: "))
            student_grade = input("Enter student grade: ")
            student_dob = input("Enter student date of birth (YYYY-MM-DD): ")
            student_subjects = [
                subject.strip()
                for subject in input(
                    "Enter student subjects (comma separated): "
                ).split(",")
                if subject.strip()
            ]

            student_info = (student_id, student_dob)
            dict1 = {
                "student_info": student_info,
                "name": student_name,
                "age": student_age,
                "grade": student_grade,
                "subjects": student_subjects,
            }
            student_list.append(dict1)

            student_dict[student_id] = {
                "name": student_name,
                "age": student_age,
                "grade": student_grade,
                "subjects": student_subjects,
            }
            student_subject.update(student_subjects)
            print("Student added successfully!\n")

        case 2:
            if len(student_list) == 0:
                print("No students to display.\n")
            else:
                print("Displaying all students...")
                for student in student_list:
                    print(
                        f" Student ID: {student['student_info'][0]}\n Student Name: {student['name']}\n Student Age: {student['age']}\n Student Grade: {student['grade']}\n Student Date of Birth: {student['student_info'][1]}\n Student Subjects: {', '.join(student['subjects'])}\n"
                    )

        case 3:
            student_id = int(input("Enter the student ID to update: "))
            found = False
            for student in student_list:
                if student["student_info"][0] == student_id:
                    found = True
                    print("What you want to update?")
                    print("1. Age")
                    print("2. Subjects")
                    choice = int(input("Enter your choice: "))
                    match choice:
                        case 1:
                            new_age = int(input("Enter new age: "))
                            student["age"] = new_age
                            student_dict[student_id]["age"] = new_age
                            print("Student age updated successfully!\n")
                        case 2:
                            new_subjects = [
                                s.strip()
                                for s in input("Enter new subjects (comma separated): ").split(",")
                                if s.strip()
                            ]
                            student["subjects"] = new_subjects
                            student_dict[student_id]["subjects"] = new_subjects
                            student_subject.update(new_subjects)
                            print("Student subjects updated successfully!\n")
                        case _:
                            print("Invalid choice\n")
                    break
            if not found:
                print("Student not found.\n")
                

        case 4:
            student_id = int(input("Enter the student ID to delete: "))
            found = False
            for student in range(len(student_list)):
                if student_list[student]["student_info"][0] == student_id:
                    found = True
                    del student_list[student]
                    del student_dict[student_id]
                    print("Student deleted successfully!\n")
                    break
            if not found:
                print("Student not found.\n")

        case 5:
            if len(student_subject) == 0:
                print("No subjects to display.\n")
            else:
                print("Subjects Offered:")
                for subject in student_subject:
                    print(subject)
                print()

        case 6:
            print("Exiting the program. Thanks to using Student Data Organizer!\n")
            break

        case _:
            print("Invalid input\n")
