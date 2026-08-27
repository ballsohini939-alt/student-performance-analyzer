import csv


def get_student_profile(name):
    """
    Find and display a complete profile of a student.
    Uses the existing project CSV files.
    """

    students = []
    subjects = []
    study_hours = None

    # -----------------------------------------
    # Load Student Data
    # -----------------------------------------
    try:
        with open("data/students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name"].strip().lower() == name.strip().lower():
                    students.append(row)

    except FileNotFoundError:
        print("\nStudent data file not found.")
        return

    if not students:
        print(f"\nNo student found with name: {name}")
        return

    student = students[0]

    # -----------------------------------------
    # Load Subject Data
    # -----------------------------------------
    try:
        with open("data/subject_marks.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name"].strip().lower() == name.strip().lower():
                    subjects.append(row)

    except FileNotFoundError:
        pass

    # -----------------------------------------
    # Load Study Hours
    # -----------------------------------------
    try:
        with open("data/study_hours.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name"].strip().lower() == name.strip().lower():
                    study_hours = float(row["StudyHours"])
                    break

    except FileNotFoundError:
        pass

    # -----------------------------------------
    # Student Performance
    # -----------------------------------------
    percentage = float(student["Percentage"])
    grade = student["Grade"]

    # Calculate total from subject marks
    total_marks = sum(
        float(row["Marks"])
        for row in subjects
    )

    # -----------------------------------------
    # Performance Category
    # -----------------------------------------
    if percentage >= 90:
        category = "Excellent"

        recommendation = (
            "Excellent performance. Maintain your current "
            "study routine and continue challenging yourself."
        )

    elif percentage >= 70:
        category = "Good"

        recommendation = (
            "Good performance. Continue practicing and "
            "focus on improving weaker subjects."
        )

    elif percentage >= 50:
        category = "Average"

        recommendation = (
            "Focus on weak subjects, practice regularly, "
            "and increase your study consistency."
        )

    else:
        category = "Needs Attention"

        recommendation = (
            "Focus on improving your fundamentals and "
            "follow a consistent study schedule."
        )

    # -----------------------------------------
    # Subject Analysis
    # -----------------------------------------
    highest_subject = None
    highest_marks = None

    lowest_subject = None
    lowest_marks = None

    if subjects:

        highest = max(
            subjects,
            key=lambda x: float(x["Marks"])
        )

        lowest = min(
            subjects,
            key=lambda x: float(x["Marks"])
        )

        highest_subject = highest["Subject"]
        highest_marks = float(highest["Marks"])

        lowest_subject = lowest["Subject"]
        lowest_marks = float(lowest["Marks"])

    # -----------------------------------------
    # Display Profile
    # -----------------------------------------
    print("\n" + "=" * 60)
    print("                 STUDENT PROFILE")
    print("=" * 60)

    # -----------------------------------------
    # Student Information
    # -----------------------------------------
    print("\nSTUDENT INFORMATION")
    print("-" * 60)

    print(f"Name        : {student['Name']}")
    print(f"Total Marks : {total_marks:.2f}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Category    : {category}")

    # -----------------------------------------
    # Subject Performance
    # -----------------------------------------
    print("\nSUBJECT PERFORMANCE")
    print("-" * 60)

    if subjects:

        for subject in subjects:

            print(
                f"{subject['Subject']:<20}"
                f"{float(subject['Marks']):>8.2f}"
            )

        print("-" * 60)

        if highest_subject:
            print(
                f"Strongest Subject : "
                f"{highest_subject} "
                f"({highest_marks:.2f})"
            )

        if lowest_subject:
            print(
                f"Weakest Subject   : "
                f"{lowest_subject} "
                f"({lowest_marks:.2f})"
            )

    else:
        print("No subject data available.")

    # -----------------------------------------
    # Learning Habits
    # -----------------------------------------
    print("\nLEARNING HABITS")
    print("-" * 60)

    if study_hours is not None:

        print(
            f"Average Study Hours : "
            f"{study_hours:.2f} hours/day"
        )

    else:

        print("Study hours data not available.")

    # -----------------------------------------
    # Personalized Recommendation
    # -----------------------------------------
    print("\nPERSONALIZED RECOMMENDATION")
    print("-" * 60)

    print(recommendation)

    # -----------------------------------------
    # Final Summary
    # -----------------------------------------
    print("\nPERFORMANCE SUMMARY")
    print("-" * 60)

    if percentage >= 90:
        print("Performance Level : Excellent")
    elif percentage >= 70:
        print("Performance Level : Good")
    elif percentage >= 50:
        print("Performance Level : Average")
    else:
        print("Performance Level : Needs Improvement")

    print("\n" + "=" * 60)