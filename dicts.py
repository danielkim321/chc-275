def getStudent(directory, student):
    if student in directory:
        return directory[student]
    else:
        return None


def getStudentGrades(directory, student):
    if student in directory:
        return directory[student]["grades"]
    else:
        return None


def getStudentGradeLevel(directory, student):
    if student in directory:
        return directory[student]["grade_level"]
    else:
        return None


def getStudentEmail(directory, student):
    if student in directory:
        return directory[student]["email"]
    else:
        return None


def getStudentsByGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["grade_level"] == gradelevel:
            print(student)


def addStudent(directory):
    name = input("Enter student name: ")
    grade_level = int(input("Enter grade level: "))
    email = input("Enter email: ")

    grades = {}
    num_classes = int(input("How many classes? "))

    for i in range(num_classes):
        subject = input("Enter subject: ")
        grade = int(input("Enter grade: "))
        grades[subject] = grade

    directory[name] = {
        "grades": grades,
        "grade_level": grade_level,
        "email": email
    }


def removeStudent(directory, student):
    if student in directory:
        del directory[student]
        print("Student removed.")
    else:
        print("Student not found.")


def updateGrade(directory, student):
    if student in directory:
        subject = input("Enter subject to update: ")
        grade = int(input("Enter new grade: "))
        directory[student]["grades"][subject] = grade
    else:
        print("Student not found.")


def calculateGPA(directory, student):
    if student not in directory:
        return 0

    grades = directory[student]["grades"]
    
    total = 0
    count = 0

    for subject in grades:
        total += grades[subject]
        count += 1

    if count == 0:
        return 0

    return total / count


def checkHonorRoll(directory, student):
    if student not in directory:
        return False

    grades = directory[student]["grades"]

    # Check all grades > 81
    for subject in grades:
        if grades[subject] <= 81:
            return False

    gpa = calculateGPA(directory, student)

    if gpa >= 88:
        return True
    else:
        return False


def printMenu():
    print("\nMenu:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student Info")
    print("4. Update Grade")
    print("5. Calculate GPA")
    print("6. Check Honor Roll")
    print("7. List Students by Grade Level")
    print("8. Quit")


def main():
    Students = {}

    while True:
        printMenu()
        choice = input("Enter choice: ")

        if choice == "1":
            addStudent(Students)

        elif choice == "2":
            name = input("Enter student name: ")
            removeStudent(Students, name)

        elif choice == "3":
            name = input("Enter student name: ")
            student = getStudent(Students, name)
            print(student)

        elif choice == "4":
            name = input("Enter student name: ")
            updateGrade(Students, name)

        elif choice == "5":
            name = input("Enter student name: ")
            print("GPA:", calculateGPA(Students, name))

        elif choice == "6":
            name = input("Enter student name: ")
            print("Honor Roll:", checkHonorRoll(Students, name))

        elif choice == "7":
            level = int(input("Enter grade level: "))
            getStudentsByGradeLevel(Students, level)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()