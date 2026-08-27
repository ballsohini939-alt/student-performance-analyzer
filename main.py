from student import Student
from analyzer import calculate_grade

from utils import (
    save_student,
    save_study_hours,
    view_students,
    search_student
)

from analytics import (
    dataset_summary,
    calculate_average,
    top_student,
    lowest_student,
    grade_statistics,
    performance_categories,
    subject_statistics,
    strongest_subject,
    weakest_subject,
    average_study_hours,
    highest_study_hours,
    lowest_study_hours,
    study_performance_analysis,
    learning_insight,
    generate_recommendations
)


def get_valid_marks(subject):
    """
    Get valid marks between 0 and 100.
    """

    while True:

        try:

            marks = float(
                input(
                    f"Enter marks for {subject}: "
                )
            )

            if 0 <= marks <= 100:

                return marks

            print(
                "Marks must be between 0 and 100."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )


def get_valid_subject_count():
    """
    Get a valid positive number of subjects.
    """

    while True:

        try:

            number = int(
                input(
                    "Enter number of subjects: "
                )
            )

            if number > 0:

                return number

            print(
                "Please enter at least one subject."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )


def get_valid_study_hours():
    """
    Get valid study hours.
    """

    while True:

        try:

            hours = float(
                input(
                    "Enter average study hours "
                    "per day: "
                )
            )

            if hours >= 0:

                return hours

            print(
                "Study hours cannot be negative."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )


def add_student():
    """
    Add or update a student's academic record.
    """

    print(
        "\n========== ADD / UPDATE STUDENT =========="
    )

    name = input(
        "Enter student name: "
    ).strip()

    if not name:

        print(
            "Student name cannot be empty."
        )

        return

    number = get_valid_subject_count()

    student = Student(name)

    print(
        "\nEnter subject-wise marks:"
    )

    for i in range(number):

        while True:

            subject = input(
                f"\nEnter subject {i + 1} name: "
            ).strip()

            if not subject:

                print(
                    "Subject name cannot be empty."
                )

                continue

            # Prevent duplicate subject names
            duplicate = any(
                existing.lower()
                == subject.lower()
                for existing
                in student.subjects
            )

            if duplicate:

                print(
                    "This subject has already "
                    "been entered."
                )

                continue

            break

        marks = get_valid_marks(subject)

        student.add_subject(
            subject,
            marks
        )

    total = student.total_marks()

    percentage = student.percentage()

    grade = calculate_grade(
        percentage
    )

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
        f"Highest      : "
        f"{student.highest_subject()}"
    )

    print(
        f"Lowest       : "
        f"{student.lowest_subject()}"
    )

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

    # Save student and subject records
    save_student(
        student,
        grade
    )

    # Save study information
    print(
        "\n========== LEARNING HABITS =========="
    )

    study_hours = get_valid_study_hours()

    save_study_hours(
        student.name,
        study_hours
    )

    print(
        "\nStudent record saved/updated successfully!"
    )

    print(
        "Academic data and study habits "
        "are synchronized."
    )


def show_menu():
    """
    Display the main menu.
    """

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


def display_dataset_summary():
    """
    Display overall dataset information.
    """

    summary = dataset_summary()

    if not summary:

        print(
            "\nNo student data available."
        )

        return

    print(
        "\nDataset Summary"
    )

    print(
        "-" * 28
    )

    print(
        f"Total Students          : "
        f"{summary['total_students']}"
    )

    print(
        f"Students With Study Data: "
        f"{summary['students_with_study_data']}"
    )

    print(
        f"Average Percentage      : "
        f"{summary['average_percentage']:.2f}%"
    )

    print(
        f"Highest Percentage      : "
        f"{summary['highest_percentage']:.2f}%"
    )

    print(
        f"Lowest Percentage       : "
        f"{summary['lowest_percentage']:.2f}%"
    )

    if summary["students_with_study_data"] > 0:

        print(
            f"Average Study Hours     : "
            f"{summary['average_study_hours']:.2f} "
            f"hours/day"
        )

    else:

        print(
            "Average Study Hours     : "
            "No data available"
        )


def display_basic_analytics():
    """
    Display class performance analytics.
    """

    average = calculate_average()

    print(
        "\nClass Average"
    )

    print(
        "-" * 28
    )

    print(
        f"{average:.2f}%"
    )

    top = top_student()

    if top:

        print(
            "\nTop Performing Student"
        )

        print(
            "-" * 28
        )

        print(
            f"Name       : {top['Name']}"
        )

        print(
            f"Percentage : "
            f"{float(top['Percentage']):.2f}%"
        )

        print(
            f"Grade      : {top['Grade']}"
        )

    lowest = lowest_student()

    if lowest:

        print(
            "\nStudent Needing Most Attention"
        )

        print(
            "-" * 28
        )

        print(
            f"Name       : {lowest['Name']}"
        )

        print(
            f"Percentage : "
            f"{float(lowest['Percentage']):.2f}%"
        )

        print(
            f"Grade      : {lowest['Grade']}"
        )


def display_grade_statistics():
    """
    Display grade distribution.
    """

    statistics = grade_statistics()

    print(
        "\nGrade Statistics"
    )

    print(
        "-" * 28
    )

    if not statistics:

        print(
            "No grade data available."
        )

        return

    for grade, count in statistics.items():

        print(
            f"{grade}: {count} student(s)"
        )


def display_performance_categories():
    """
    Display performance categories.
    """

    categories = performance_categories()

    print(
        "\nPerformance Categories"
    )

    print(
        "-" * 28
    )

    for category, count in categories.items():

        print(
            f"{category}: "
            f"{count} student(s)"
        )


def display_subject_statistics():
    """
    Display subject-wise performance.
    """

    statistics = subject_statistics()

    print(
        "\nSubject Performance"
    )

    print(
        "-" * 28
    )

    if not statistics:

        print(
            "No subject data available."
        )

        return

    for subject, average in sorted(
        statistics.items()
    ):

        print(
            f"{subject:<15}"
            f"Average: {average:.2f}%"
        )

    strongest = strongest_subject()

    weakest = weakest_subject()

    if strongest:

        print(
            f"\nStrongest Subject : "
            f"{strongest}"
        )

    if weakest:

        print(
            f"Weakest Subject   : "
            f"{weakest}"
        )


def display_learning_habits():
    """
    Display study-hour analytics.
    """

    average_hours = average_study_hours()

    highest = highest_study_hours()

    lowest = lowest_study_hours()

    print(
        "\nLearning Habits"
    )

    print(
        "-" * 28
    )

    if not highest:

        print(
            "No study-hour data available."
        )

        return

    print(
        f"Average Study Hours : "
        f"{average_hours:.2f} hours/day"
    )

    print(
        f"Highest Study Time  : "
        f"{highest['Name']} "
        f"({float(highest['StudyHours']):.2f} "
        f"hours/day)"
    )

    print(
        f"Lowest Study Time   : "
        f"{lowest['Name']} "
        f"({float(lowest['StudyHours']):.2f} "
        f"hours/day)"
    )


def display_study_performance():
    """
    Display study hours versus academic performance.
    """

    data = study_performance_analysis()

    print(
        "\nStudy Hours vs Performance"
    )

    print(
        "-" * 28
    )

    if not data:

        print(
            "No matching study and "
            "performance data available."
        )

        return

    for student in data:

        print(
            f"{student['Name']:<12}"
            f"Study: "
            f"{student['StudyHours']:.2f} hrs/day   "
            f"Score: "
            f"{student['Percentage']:.2f}%"
        )


def display_learning_insight():
    """
    Display learning pattern insight.
    """

    insight = learning_insight()

    print(
        "\nLearning Insight"
    )

    print(
        "-" * 28
    )

    print(
        insight
    )


def display_recommendations():
    """
    Display personalized recommendations.
    """

    recommendations = (
        generate_recommendations()
    )

    print(
        "\nPersonalized Learning Recommendations"
    )

    print(
        "-" * 40
    )

    if not recommendations:

        print(
            "No recommendation data available."
        )

        return

    for name, items in recommendations.items():

        print(
            f"\n{name}:"
        )

        for recommendation in items:

            print(
                f"  • {recommendation}"
            )


def view_analytics():
    """
    Display complete advanced analytics.
    """

    print(
        "\n========== ADVANCED ANALYTICS =========="
    )

    display_dataset_summary()

    display_basic_analytics()

    display_grade_statistics()

    display_performance_categories()

    display_subject_statistics()

    display_learning_habits()

    display_study_performance()

    display_learning_insight()

    display_recommendations()

    print(
        "\n=========================================="
    )


def main():
    """
    Main application loop.
    """

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            name = input(
                "Enter student name to search: "
            ).strip()

            if name:

                search_student(name)

            else:

                print(
                    "\nStudent name cannot be empty."
                )

        elif choice == "4":

            view_analytics()

        elif choice == "5":

            print(
                "\nThank you for using "
                "Student Performance Analyzer."
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-5."
            )


if __name__ == "__main__":

    main()