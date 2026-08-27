from student import Student
from analyzer import calculate_grade

from utils import (
    save_student,
    save_study_hours,
    view_students,
    search_student
)

from analytics import (
    calculate_average,
    top_student,
    grade_statistics
)


def add_student():

    print("\n========== ADD STUDENT ==========")

    # -------------------------------
    # Student Name
    # -------------------------------

    while True:

        name = input("Enter student name: ").strip()

        try:
            student = Student(name)
            break

        except ValueError as error:
            print(f"Error: {error}")

    # -------------------------------
    # Number of Subjects
    # -------------------------------

    while True:

        try:

            number = int(
                input("Enter number of subjects: ")
            )

            if number > 0:
                break

            print("Please enter at least one subject.")

        except ValueError:

            print(
                "Please enter a valid whole number."
            )

    # -------------------------------
    # Subject and Marks
    # -------------------------------

    for i in range(number):

        while True:

            subject = input(
                f"\nEnter subject {i + 1} name: "
            ).strip()

            if not subject:

                print(
                    "Error: Subject name cannot be empty."
                )

                continue

            try:

                marks = float(
                    input(
                        f"Enter marks for {subject}: "
                    )
                )

                student.add_subject(
                    subject,
                    marks
                )

                break

            except ValueError as error:

                print(
                    f"Error: {error}"
                )

    # -------------------------------
    # Study Hours
    # -------------------------------

    while True:

        try:

            study_hours = float(
                input(
                    "\nEnter average study hours per day: "
                )
            )

            if study_hours < 0:

                print(
                    "Study hours cannot be negative."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # -------------------------------
    # Performance Calculation
    # -------------------------------

    total = student.total_marks()

    percentage = student.percentage()

    grade = calculate_grade(
        percentage
    )

    # -------------------------------
    # Performance Report
    # -------------------------------

    print(
        "\n========== PERFORMANCE REPORT =========="
    )

    print(
        f"Student Name : {student.name}"
    )

    print(
        f"Total Marks  : {total:.2f}"
    )

    print(
        f"Percentage   : {percentage:.2f}%"
    )

    print(
        f"Grade        : {grade}"
    )

    print(
        f"Highest      : {student.highest_subject()}"
    )

    print(
        f"Lowest       : {student.lowest_subject()}"
    )

    print(
        f"Study Hours  : {study_hours:.2f} hours/day"
    )

    # -------------------------------
    # Subject-wise Marks
    # -------------------------------

    print(
        "\nSubject-wise Marks"
    )

    print(
        "-" * 30
    )

    for subject, marks in student.subjects.items():

        print(
            f"{subject:<15}{marks:.2f}"
        )

    # -------------------------------
    # Save Data
    # -------------------------------

    save_student(
        student,
        grade
    )

    save_study_hours(
        student.name,
        study_hours
    )

    print(
        "\nStudent record saved successfully!"
    )


def show_analytics():

    print(
        "\n========== ANALYTICS =========="
    )

    # -------------------------------
    # Class Average
    # -------------------------------

    average = calculate_average()

    if average == 0:

        print(
            "\nNo student data available."
        )

        return

    print(
        f"\nClass Average: {average:.2f}%"
    )

    # -------------------------------
    # Top Student
    # -------------------------------

    student = top_student()

    if student:

        print(
            "\nTop Performing Student"
        )

        print(
            "----------------------------"
        )

        print(
            f"Name       : {student['Name']}"
        )

        print(
            f"Percentage : {student['Percentage']}%"
        )

        print(
            f"Grade      : {student['Grade']}"
        )

    # -------------------------------
    # Grade Statistics
    # -------------------------------

    statistics = grade_statistics()

    print(
        "\nGrade Statistics"
    )

    print(
        "----------------------------"
    )

    for grade, count in statistics.items():

        print(
            f"{grade}: {count} student(s)"
        )

    print(
        "=============================="
    )


def show_menu():

    print(
        "\n" + "=" * 40
    )

    print(
        "     STUDENT PERFORMANCE ANALYZER"
    )

    print(
        "=" * 40
    )

    print(
        "1. Add Student"
    )

    print(
        "2. View All Students"
    )

    print(
        "3. Search Student"
    )

    print(
        "4. View Analytics"
    )

    print(
        "5. Exit"
    )


def main():

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # -------------------------------
        # Add Student
        # -------------------------------

        if choice == "1":

            add_student()

        # -------------------------------
        # View Students
        # -------------------------------

        elif choice == "2":

            view_students()

        # -------------------------------
        # Search Student
        # -------------------------------

        elif choice == "3":

            name = input(
                "Enter student name to search: "
            ).strip()

            if not name:

                print(
                    "\nError: Student name cannot be empty."
                )

            else:

                search_student(name)

        # -------------------------------
        # Analytics
        # -------------------------------

        elif choice == "4":

            show_analytics()

        # -------------------------------
        # Exit
        # -------------------------------

        elif choice == "5":

            print(
                "\nThank you for using "
                "Student Performance Analyzer."
            )

            break

        # -------------------------------
        # Invalid Menu Choice
        # -------------------------------

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 5."
            )


if __name__ == "__main__":
    main()