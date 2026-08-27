import csv
import os


def load_students():
    """Load student academic data from CSV."""

    file_path = "data/students.csv"

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_subject_marks():
    """Load subject-wise marks from CSV."""

    file_path = "data/subject_marks.csv"

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_study_hours():
    """Load study-hour data from CSV."""

    file_path = "data/study_hours.csv"

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def calculate_categories(students):
    """Calculate student performance categories."""

    categories = {
        "Excellent": 0,
        "Good": 0,
        "Average": 0,
        "Needs Attention": 0
    }

    for student in students:
        try:
            percentage = float(student["Percentage"])
        except (ValueError, KeyError):
            continue

        if percentage >= 90:
            categories["Excellent"] += 1
        elif percentage >= 70:
            categories["Good"] += 1
        elif percentage >= 50:
            categories["Average"] += 1
        else:
            categories["Needs Attention"] += 1

    return categories


def calculate_subject_averages(subject_data):
    """Calculate average marks for every subject."""

    subject_marks = {}

    for row in subject_data:
        try:
            subject = row["Subject"]
            marks = float(row["Marks"])
        except (ValueError, KeyError):
            continue

        if subject not in subject_marks:
            subject_marks[subject] = []

        subject_marks[subject].append(marks)

    subject_averages = {}

    for subject, marks in subject_marks.items():
        if marks:
            subject_averages[subject] = sum(marks) / len(marks)

    return subject_averages


def display_class_dashboard():
    """Display the complete class performance dashboard."""

    students = load_students()
    subject_data = load_subject_marks()
    study_data = load_study_hours()

    print("\n" + "=" * 60)
    print("              CLASS PERFORMANCE DASHBOARD")
    print("=" * 60)

    if not students:
        print("\nNo student data available.")
        print("=" * 60)
        return

    # --------------------------------------------------
    # Basic Class Statistics
    # --------------------------------------------------

    percentages = []

    for student in students:
        try:
            percentages.append(float(student["Percentage"]))
        except (ValueError, KeyError):
            continue

    print("\nCLASS OVERVIEW")
    print("-" * 60)

    print(f"Total Students       : {len(students)}")

    if percentages:
        average = sum(percentages) / len(percentages)

        print(f"Class Average        : {average:.2f}%")
        print(f"Highest Percentage    : {max(percentages):.2f}%")
        print(f"Lowest Percentage     : {min(percentages):.2f}%")

    # --------------------------------------------------
    # Top Student
    # --------------------------------------------------

    valid_students = []

    for student in students:
        try:
            percentage = float(student["Percentage"])
            valid_students.append((student, percentage))
        except (ValueError, KeyError):
            continue

    if valid_students:

        top_student, top_percentage = max(
            valid_students,
            key=lambda item: item[1]
        )

        lowest_student, lowest_percentage = min(
            valid_students,
            key=lambda item: item[1]
        )

        print("\nTOP PERFORMER")
        print("-" * 60)

        print(f"Name                 : {top_student['Name']}")
        print(f"Percentage           : {top_percentage:.2f}%")
        print(f"Grade                : {top_student['Grade']}")

        print("\nSTUDENT NEEDING MOST ATTENTION")
        print("-" * 60)

        print(f"Name                 : {lowest_student['Name']}")
        print(f"Percentage           : {lowest_percentage:.2f}%")
        print(f"Grade                : {lowest_student['Grade']}")

    # --------------------------------------------------
    # Grade Distribution
    # --------------------------------------------------

    grade_distribution = {}

    for student in students:
        grade = student.get("Grade", "Unknown")

        if grade not in grade_distribution:
            grade_distribution[grade] = 0

        grade_distribution[grade] += 1

    print("\nGRADE DISTRIBUTION")
    print("-" * 60)

    for grade, count in sorted(grade_distribution.items()):
        print(f"{grade:<20}: {count} student(s)")

    # --------------------------------------------------
    # Performance Categories
    # --------------------------------------------------

    categories = calculate_categories(students)

    print("\nPERFORMANCE CATEGORIES")
    print("-" * 60)

    for category, count in categories.items():
        print(f"{category:<20}: {count} student(s)")

    # --------------------------------------------------
    # Subject Performance
    # --------------------------------------------------

    subject_averages = calculate_subject_averages(subject_data)

    print("\nSUBJECT PERFORMANCE")
    print("-" * 60)

    if subject_averages:

        for subject, average_marks in sorted(
            subject_averages.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(
                f"{subject:<20}: "
                f"{average_marks:.2f}%"
            )

        strongest_subject = max(
            subject_averages,
            key=subject_averages.get
        )

        weakest_subject = min(
            subject_averages,
            key=subject_averages.get
        )

        print(
            f"\nStrongest Subject    : "
            f"{strongest_subject} "
            f"({subject_averages[strongest_subject]:.2f}%)"
        )

        print(
            f"Weakest Subject      : "
            f"{weakest_subject} "
            f"({subject_averages[weakest_subject]:.2f}%)"
        )

    else:
        print("No subject data available.")

    # --------------------------------------------------
    # Study Habits
    # --------------------------------------------------

    study_hours = []

    for row in study_data:
        try:
            study_hours.append(float(row["StudyHours"]))
        except (ValueError, KeyError):
            continue

    print("\nLEARNING HABITS")
    print("-" * 60)

    if study_hours:

        average_hours = sum(study_hours) / len(study_hours)

        print(
            f"Average Study Hours  : "
            f"{average_hours:.2f} hours/day"
        )

        print(
            f"Highest Study Hours  : "
            f"{max(study_hours):.2f} hours/day"
        )

        print(
            f"Lowest Study Hours   : "
            f"{min(study_hours):.2f} hours/day"
        )

    else:
        print("No study-hour data available.")

    # --------------------------------------------------
    # Class Insight
    # --------------------------------------------------

    print("\nCLASS INSIGHT")
    print("-" * 60)

    if percentages:

        average = sum(percentages) / len(percentages)

        excellent = categories["Excellent"]
        needs_attention = categories["Needs Attention"]

        if average >= 90:
            print(
                "The class is performing at an excellent level."
            )

        elif average >= 70:
            print(
                "The class is performing at a good level."
            )

        elif average >= 50:
            print(
                "The class has average performance."
            )

        else:
            print(
                "The class needs significant academic improvement."
            )

        if excellent > 0:
            print(
                f"{excellent} student(s) are currently "
                "in the Excellent category."
            )

        if needs_attention > 0:
            print(
                f"{needs_attention} student(s) need "
                "additional academic attention."
            )

    # --------------------------------------------------
    # Dashboard Footer
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("             END OF CLASS DASHBOARD")
    print("=" * 60)