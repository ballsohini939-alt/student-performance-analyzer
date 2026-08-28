
import csv


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_performance_category(percentage):
    """Return the performance category."""

    if percentage >= 90:
        return "Excellent"

    elif percentage >= 70:
        return "Good"

    elif percentage >= 50:
        return "Average"

    else:
        return "Needs Attention"


def get_recommendation(percentage):
    """Return a personalized academic recommendation."""

    if percentage >= 90:

        return (
            "Excellent performance. Maintain your current "
            "study routine and continue challenging yourself."
        )

    elif percentage >= 70:

        return (
            "Good performance. Continue practicing and "
            "focus on improving weaker subjects."
        )

    elif percentage >= 50:

        return (
            "Focus on weak subjects, practice regularly, "
            "and increase your study consistency."
        )

    else:

        return (
            "Focus on improving your fundamentals and "
            "follow a consistent study schedule."
        )


def get_study_assessment(study_hours):
    """Assess the student's study commitment."""

    if study_hours is None:
        return "Study-hour data is not available."

    if study_hours >= 8:
        return "Excellent study commitment."

    elif study_hours >= 5:
        return "Good study commitment."

    elif study_hours >= 3:
        return "Moderate study commitment. Consider increasing consistency."

    else:
        return "Low study commitment. Try following a regular study schedule."


# ============================================================
# STUDENT PROFILE
# ============================================================

def get_student_profile(name):
    """
    Find and display a complete profile of a student.

    Includes:
    - Student information
    - Subject performance
    - Strongest subject
    - Weakest subject
    - Learning habits
    - Performance assessment
    - Personalized recommendation
    - Learning insights
    """

    students = []
    subjects = []
    study_hours = None

    # ========================================================
    # LOAD STUDENT DATA
    # ========================================================

    try:

        with open(
            "data/students.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                if (
                    row["Name"].strip().lower()
                    == name.strip().lower()
                ):

                    students.append(row)

    except FileNotFoundError:

        print("\nStudent data file not found.")

        return

    if not students:

        print(
            f"\nNo student found with name: {name}"
        )

        return

    student = students[0]

    # ========================================================
    # LOAD SUBJECT DATA
    # ========================================================

    try:

        with open(
            "data/subject_marks.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                if (
                    row["Name"].strip().lower()
                    == name.strip().lower()
                ):

                    try:

                        subjects.append(
                            {
                                "Subject": row["Subject"],
                                "Marks": float(row["Marks"])
                            }
                        )

                    except ValueError:

                        continue

    except FileNotFoundError:

        pass

    # ========================================================
    # LOAD STUDY HOURS
    # ========================================================

    try:

        with open(
            "data/study_hours.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                if (
                    row["Name"].strip().lower()
                    == name.strip().lower()
                ):

                    try:

                        study_hours = float(
                            row["StudyHours"]
                        )

                    except ValueError:

                        study_hours = None

                    break

    except FileNotFoundError:

        pass

    # ========================================================
    # BASIC PERFORMANCE DATA
    # ========================================================

    try:

        percentage = float(
            student["Percentage"]
        )

    except (
        KeyError,
        ValueError
    ):

        percentage = 0.0

    grade = student.get(
        "Grade",
        "N/A"
    )

    # ========================================================
    # TOTAL MARKS
    # ========================================================

    if subjects:

        total_marks = sum(
            subject["Marks"]
            for subject in subjects
        )

    else:

        try:

            total_marks = float(
                student["Total"]
            )

        except (
            KeyError,
            ValueError
        ):

            total_marks = 0.0

    # ========================================================
    # PERFORMANCE CATEGORY
    # ========================================================

    category = get_performance_category(
        percentage
    )

    recommendation = get_recommendation(
        percentage
    )

    # ========================================================
    # SUBJECT ANALYSIS
    # ========================================================

    highest_subject = None
    highest_marks = None

    lowest_subject = None
    lowest_marks = None

    if subjects:

        highest = max(
            subjects,
            key=lambda x: x["Marks"]
        )

        lowest = min(
            subjects,
            key=lambda x: x["Marks"]
        )

        highest_subject = highest["Subject"]
        highest_marks = highest["Marks"]

        lowest_subject = lowest["Subject"]
        lowest_marks = lowest["Marks"]

    # ========================================================
    # LEARNING INSIGHTS
    # ========================================================

    insights = []

    if highest_subject:

        insights.append(
            f"You are strongest in {highest_subject} "
            f"with a score of {highest_marks:.2f}%."
        )

    if lowest_subject:

        insights.append(
            f"{lowest_subject} is your weakest subject "
            f"with a score of {lowest_marks:.2f}%."
        )

    if study_hours is not None:

        study_assessment = get_study_assessment(
            study_hours
        )

        insights.append(
            study_assessment
        )

    if percentage >= 90:

        insights.append(
            "You are performing at an excellent academic level."
        )

    elif percentage >= 70:

        insights.append(
            "You have a good academic foundation with "
            "room for further improvement."
        )

    elif percentage >= 50:

        insights.append(
            "Improving your weaker subjects can significantly "
            "increase your overall performance."
        )

    else:

        insights.append(
            "Focus on strengthening your fundamentals and "
            "building a consistent learning routine."
        )

    # ========================================================
    # DISPLAY PROFILE
    # ========================================================

    print(
        "\n" + "=" * 65
    )

    print(
        "                    STUDENT PROFILE"
    )

    print(
        "=" * 65
    )

    # ========================================================
    # STUDENT INFORMATION
    # ========================================================

    print(
        "\nSTUDENT INFORMATION"
    )

    print(
        "-" * 65
    )

    print(
        f"Name        : {student['Name']}"
    )

    print(
        f"Total Marks : {total_marks:.2f}"
    )

    print(
        f"Percentage  : {percentage:.2f}%"
    )

    print(
        f"Grade       : {grade}"
    )

    print(
        f"Category    : {category}"
    )

    # ========================================================
    # PERFORMANCE SUMMARY
    # ========================================================

    print(
        "\nPERFORMANCE SUMMARY"
    )

    print(
        "-" * 65
    )

    if percentage >= 90:

        print(
            "Overall Assessment : Outstanding academic performance."
        )

    elif percentage >= 70:

        print(
            "Overall Assessment : Good academic performance."
        )

    elif percentage >= 50:

        print(
            "Overall Assessment : Average academic performance."
        )

    else:

        print(
            "Overall Assessment : Academic improvement required."
        )

    # ========================================================
    # SUBJECT PERFORMANCE
    # ========================================================

    print(
        "\nSUBJECT PERFORMANCE"
    )

    print(
        "-" * 65
    )

    if subjects:

        print(
            f"{'Subject':<25}"
            f"{'Marks':>12}"
        )

        print(
            "-" * 65
        )

        for subject in subjects:

            print(
                f"{subject['Subject']:<25}"
                f"{subject['Marks']:>12.2f}"
            )

        print(
            "-" * 65
        )

        if highest_subject:

            print(
                f"Strongest Subject : "
                f"{highest_subject} "
                f"({highest_marks:.2f}%)"
            )

        if lowest_subject:

            print(
                f"Weakest Subject   : "
                f"{lowest_subject} "
                f"({lowest_marks:.2f}%)"
            )

    else:

        print(
            "No subject data available."
        )

    # ========================================================
    # LEARNING HABITS
    # ========================================================

    print(
        "\nLEARNING HABITS"
    )

    print(
        "-" * 65
    )

    if study_hours is not None:

        print(
            f"Average Study Hours : "
            f"{study_hours:.2f} hours/day"
        )

        print(
            f"Assessment          : "
            f"{get_study_assessment(study_hours)}"
        )

    else:

        print(
            "Study hours data not available."
        )

    # ========================================================
    # PERSONALIZED RECOMMENDATION
    # ========================================================

    print(
        "\nPERSONALIZED RECOMMENDATION"
    )

    print(
        "-" * 65
    )

    print(
        recommendation
    )

    # ========================================================
    # LEARNING INSIGHTS
    # ========================================================

    print(
        "\nLEARNING INSIGHTS"
    )

    print(
        "-" * 65
    )

    if insights:

        for index, insight in enumerate(
            insights,
            start=1
        ):

            print(
                f"{index}. {insight}"
            )

    else:

        print(
            "No additional learning insights available."
        )

    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print(
        "\nFINAL SUMMARY"
    )

    print(
        "-" * 65
    )

    print(
        f"Student             : {student['Name']}"
    )

    print(
        f"Overall Percentage  : {percentage:.2f}%"
    )

    print(
        f"Grade               : {grade}"
    )

    print(
        f"Performance Level   : {category}"
    )

    if highest_subject:

        print(
            f"Strongest Subject   : "
            f"{highest_subject} ({highest_marks:.2f}%)"
        )

    if lowest_subject:

        print(
            f"Weakest Subject     : "
            f"{lowest_subject} ({lowest_marks:.2f}%)"
        )

    if study_hours is not None:

        print(
            f"Study Hours         : "
            f"{study_hours:.2f} hours/day"
        )

    print(
        "\n" + "=" * 65
    )

