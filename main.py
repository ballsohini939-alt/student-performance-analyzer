from student import Student
from analyzer import calculate_grade
from utils import save_student, view_students, search_student
from analytics import calculate_average, top_student, grade_statistics


def add_student():
    print("\n========== ADD STUDENT ==========")

    # Get and validate student name
    while True:
        name = input("Enter student name: ").strip()

        try:
            student = Student(name)
            break
        except ValueError as error:
            print(f"Error: {error}")

    # Get and validate number of subjects
    while True:
        try:
            number = int(input("Enter number of subjects: "))

            if number > 0:
                break

            print("Please enter at least one subject.")

        except ValueError:
            print("Please enter a valid whole number.")

    # Enter subject details
    for i in range(number):

        while True:
            subject = input(
                f"\nEnter subject {i + 1} name: "
            ).strip()

            if not subject:
                print("Error: Subject name cannot be empty.")
                continue

            try:
                marks = float(
                    input(f"Enter marks for {subject}: ")
                )

                student.add_subject(subject, marks)
                break

            except ValueError as error:
                print(f"Error: {error}")

    # Calculate performance
    total = student.total_marks()
    percentage = student.percentage()
    grade = calculate_grade(percentage)

    # Display performance report
    print("\n========== PERFORMANCE REPORT ==========")
    print(f"Student Name : {student.name}")
    print(f"Total Marks  : {total:.2f}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Highest      : {student.highest_subject()}")
    print(f"Lowest       : {student.lowest_subject()}")

    print("\nSubject-wise Marks")
    print("-" * 30)

    for subject, marks in student.subjects.items():
        print(f"{subject:<15}{marks:.2f}")

    # Save student data
    save_student(student, grade)

    print("\nStudent record saved successfully!")


def show_analytics():
    print("\n========== ANALYTICS ==========")

    # Class average
    average = calculate_average()

    if average == 0:
        print("\nNo student data available.")
        return

    print(f"\nClass Average: {average:.2f}%")

    # Top student
    student = top_student()

    if student:
        print("\nTop Performing Student")
        print("----------------------------")
        print(f"Name       : {student['Name']}")
        print(f"Percentage : {student['Percentage']}%")
        print(f"Grade      : {student['Grade']}")

    # Grade statistics
    statistics = grade_statistics()

    print("\nGrade Statistics")
    print("----------------------------")

    for grade, count in statistics.items():
        print(f"{grade}: {count} student(s)")

    print("==============================")


def show_menu():
    print("\n" + "=" * 40)
    print("     STUDENT PERFORMANCE ANALYZER")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. View Analytics")
    print("5. Exit")


def main():

    while True:

        show_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            name = input("Enter student name to search: ").strip()

            if not name:
                print("\nError: Student name cannot be empty.")
            else:
                search_student(name)

        elif choice == "4":
            show_analytics()

        elif choice == "5":
            print("\nThank you for using Student Performance Analyzer.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()