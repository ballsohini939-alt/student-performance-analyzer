
import csv
import os


# ============================================================
# FILE PATHS
# ============================================================

STUDENTS_FILE = "data/students.csv"
SUBJECT_MARKS_FILE = "data/subject_marks.csv"
STUDY_HOURS_FILE = "data/study_hours.csv"


# ============================================================
# LOAD DATA
# ============================================================

def load_csv(file_path):
    """Load records from a CSV file safely."""

    if not os.path.exists(file_path):
        return []

    try:
        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)
            return list(reader)

    except (
        OSError,
        csv.Error
    ):
        return []


def load_students():
    """Load student academic data from CSV."""

    return load_csv(STUDENTS_FILE)


def load_subject_marks():
    """Load subject-wise marks from CSV."""

    return load_csv(SUBJECT_MARKS_FILE)


def load_study_hours():
    """Load study-hour data from CSV."""

    return load_csv(STUDY_HOURS_FILE)


# ============================================================
# PERFORMANCE CATEGORY
# ============================================================

def get_performance_category(percentage):
    """Return performance category based on percentage."""

    if percentage >= 90:
        return "Excellent"

    elif percentage >= 70:
        return "Good"

    elif percentage >= 50:
        return "Average"

    else:
        return "Needs Attention"


# ============================================================
# VALID STUDENT DATA
# ============================================================

def get_valid_students(students):
    """Return students with valid percentage data."""

    valid_students = []

    for student in students:

        try:
            percentage = float(
                student["Percentage"]
            )

            valid_students.append(
                (
                    student,
                    percentage
                )
            )

        except (
            ValueError,
            KeyError,
            TypeError
        ):
            continue

    return valid_students


# ============================================================
# PERFORMANCE CATEGORIES
# ============================================================

def calculate_categories(students):
    """Calculate student performance categories."""

    categories = {
        "Excellent": 0,
        "Good": 0,
        "Average": 0,
        "Needs Attention": 0
    }

    valid_students = get_valid_students(
        students
    )

    for student, percentage in valid_students:

        category = get_performance_category(
            percentage
        )

        categories[category] += 1

    return categories


# ============================================================
# GRADE DISTRIBUTION
# ============================================================

def calculate_grade_distribution(students):
    """Calculate grade distribution."""

    distribution = {}

    for student in students:

        grade = student.get(
            "Grade",
            "Unknown"
        ).strip()

        if not grade:
            grade = "Unknown"

        distribution[grade] = (
            distribution.get(
                grade,
                0
            ) + 1
        )

    return distribution


# ============================================================
# SUBJECT AVERAGES
# ============================================================

def calculate_subject_averages(subject_data):
    """Calculate average marks for every subject."""

    subject_marks = {}

    for row in subject_data:

        try:
            subject = row["Subject"].strip()
            marks = float(row["Marks"])

        except (
            ValueError,
            KeyError,
            TypeError,
            AttributeError
        ):
            continue

        if not subject:
            continue

        if subject not in subject_marks:
            subject_marks[subject] = []

        subject_marks[subject].append(
            marks
        )

    subject_averages = {}

    for subject, marks in subject_marks.items():

        if marks:
            subject_averages[subject] = (
                sum(marks) / len(marks)
            )

    return subject_averages


# ============================================================
# STUDY STATISTICS
# ============================================================

def calculate_study_statistics(study_data):
    """Calculate class study-hour statistics."""

    valid_records = []

    for row in study_data:

        try:
            name = row["Name"].strip()
            hours = float(row["StudyHours"])

            valid_records.append(
                (
                    name,
                    hours
                )
            )

        except (
            ValueError,
            KeyError,
            TypeError,
            AttributeError
        ):
            continue

    if not valid_records:
        return None

    hours = [
        record[1]
        for record in valid_records
    ]

    average = (
        sum(hours) / len(hours)
    )

    highest = max(
        valid_records,
        key=lambda item: item[1]
    )

    lowest = min(
        valid_records,
        key=lambda item: item[1]
    )

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "records": valid_records
    }


# ============================================================
# STUDENTS NEEDING ATTENTION
# ============================================================

def get_students_needing_attention(students):
    """Return students below 50 percent."""

    attention_students = []

    for student, percentage in get_valid_students(
        students
    ):

        if percentage < 50:
            attention_students.append(
                (
                    student,
                    percentage
                )
            )

    return sorted(
        attention_students,
        key=lambda item: item[1]
    )


# ============================================================
# CLASS RECOMMENDATIONS
# ============================================================

def generate_class_recommendations(
    average,
    categories,
    weakest_subject,
    study_statistics
):
    """Generate useful class-level recommendations."""

    recommendations = []

    if categories["Needs Attention"] > 0:

        recommendations.append(
            "Provide additional academic support "
            "to students below 50%."
        )

    if weakest_subject:

        recommendations.append(
            f"Provide additional practice and "
            f"support in {weakest_subject}."
        )

    if study_statistics:

        if study_statistics["average"] < 4:

            recommendations.append(
                "Encourage students to increase "
                "their daily study consistency."
            )

        else:

            recommendations.append(
                "Encourage students to maintain "
                "a consistent study routine."
            )

    if categories["Excellent"] > 0:

        recommendations.append(
            "Provide advanced practice and "
            "challenging tasks to high-performing students."
        )

    if average >= 90:

        recommendations.append(
            "Maintain the current academic standards "
            "and encourage continuous improvement."
        )

    elif average >= 70:

        recommendations.append(
            "Focus on moving good-performing students "
            "towards the excellent category."
        )

    elif average >= 50:

        recommendations.append(
            "Increase revision, practice, and "
            "subject-specific support."
        )

    else:

        recommendations.append(
            "Implement a structured academic "
            "improvement plan for the class."
        )

    return recommendations


# ============================================================
# DISPLAY CLASS DASHBOARD
# ============================================================

def display_class_dashboard():
    """Display the complete class performance dashboard."""

    students = load_students()
    subject_data = load_subject_marks()
    study_data = load_study_hours()

    print("\n" + "=" * 70)
    print(
        "                 CLASS PERFORMANCE DASHBOARD"
    )
    print("=" * 70)

    if not students:

        print(
            "\nNo student data available."
        )

        print("=" * 70)

        return

    # ========================================================
    # BASIC STATISTICS
    # ========================================================

    valid_students = get_valid_students(
        students
    )

    percentages = [
        percentage
        for student, percentage
        in valid_students
    ]

    print("\nCLASS OVERVIEW")
    print("-" * 70)

    print(
        f"Total Students       : {len(students)}"
    )

    print(
        f"Valid Performance Records: "
        f"{len(valid_students)}"
    )

    if percentages:

        class_average = (
            sum(percentages)
            / len(percentages)
        )

        highest_percentage = max(
            percentages
        )

        lowest_percentage = min(
            percentages
        )

        print(
            f"Class Average        : "
            f"{class_average:.2f}%"
        )

        print(
            f"Highest Percentage   : "
            f"{highest_percentage:.2f}%"
        )

        print(
            f"Lowest Percentage    : "
            f"{lowest_percentage:.2f}%"
        )

    else:

        class_average = 0

        print(
            "No valid percentage data available."
        )

    # ========================================================
    # TOP PERFORMERS
    # ========================================================

    if valid_students:

        ranked_students = sorted(
            valid_students,
            key=lambda item: item[1],
            reverse=True
        )

        print("\nTOP PERFORMERS")
        print("-" * 70)

        top_count = min(
            3,
            len(ranked_students)
        )

        for index in range(top_count):

            student, percentage = (
                ranked_students[index]
            )

            print(
                f"{index + 1}. "
                f"{student['Name']} - "
                f"{percentage:.2f}% "
                f"(Grade: {student.get('Grade', 'N/A')})"
            )

        lowest_student, lowest_percentage = (
            ranked_students[-1]
        )

        print(
            "\nSTUDENT NEEDING MOST ATTENTION"
        )

        print("-" * 70)

        print(
            f"Name                 : "
            f"{lowest_student['Name']}"
        )

        print(
            f"Percentage           : "
            f"{lowest_percentage:.2f}%"
        )

        print(
            f"Grade                : "
            f"{lowest_student.get('Grade', 'N/A')}"
        )

    # ========================================================
    # PASS / FAIL
    # ========================================================

    print("\nPASS / PERFORMANCE STATUS")
    print("-" * 70)

    passed = sum(
        1
        for percentage in percentages
        if percentage >= 50
    )

    failed = sum(
        1
        for percentage in percentages
        if percentage < 50
    )

    print(
        f"Students Passed      : {passed}"
    )

    print(
        f"Students Below 50%   : {failed}"
    )

    if percentages:

        pass_rate = (
            passed / len(percentages)
        ) * 100

        print(
            f"Class Pass Rate      : "
            f"{pass_rate:.2f}%"
        )

    # ========================================================
    # GRADE DISTRIBUTION
    # ========================================================

    grade_distribution = (
        calculate_grade_distribution(
            students
        )
    )

    print("\nGRADE DISTRIBUTION")
    print("-" * 70)

    for grade, count in sorted(
        grade_distribution.items()
    ):

        print(
            f"{grade:<20}: "
            f"{count} student(s)"
        )

    # ========================================================
    # PERFORMANCE CATEGORIES
    # ========================================================

    categories = calculate_categories(
        students
    )

    print("\nPERFORMANCE CATEGORIES")
    print("-" * 70)

    for category, count in categories.items():

        print(
            f"{category:<20}: "
            f"{count} student(s)"
        )

    # ========================================================
    # SUBJECT PERFORMANCE
    # ========================================================

    subject_averages = (
        calculate_subject_averages(
            subject_data
        )
    )

    print("\nSUBJECT PERFORMANCE")
    print("-" * 70)

    strongest_subject = None
    weakest_subject = None

    if subject_averages:

        sorted_subjects = sorted(
            subject_averages.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for subject, average_marks in (
            sorted_subjects
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

        print(
            "No subject data available."
        )

    # ========================================================
    # LEARNING HABITS
    # ========================================================

    study_statistics = (
        calculate_study_statistics(
            study_data
        )
    )

    print("\nLEARNING HABITS")
    print("-" * 70)

    if study_statistics:

        print(
            f"Average Study Hours  : "
            f"{study_statistics['average']:.2f} hours/day"
        )

        print(
            f"Highest Study Hours  : "
            f"{study_statistics['highest'][0]} "
            f"({study_statistics['highest'][1]:.2f} hours/day)"
        )

        print(
            f"Lowest Study Hours   : "
            f"{study_statistics['lowest'][0]} "
            f"({study_statistics['lowest'][1]:.2f} hours/day)"
        )

    else:

        print(
            "No study-hour data available."
        )

    # ========================================================
    # STUDENTS NEEDING ATTENTION
    # ========================================================

    attention_students = (
        get_students_needing_attention(
            students
        )
    )

    print(
        "\nSTUDENTS NEEDING ACADEMIC ATTENTION"
    )

    print("-" * 70)

    if attention_students:

        for student, percentage in (
            attention_students
        ):

            print(
                f"{student['Name']:<20} "
                f"{percentage:.2f}% "
                f"Grade: {student.get('Grade', 'N/A')}"
            )

    else:

        print(
            "No students currently require "
            "significant academic attention."
        )

    # ========================================================
    # CLASS INSIGHT
    # ========================================================

    print("\nCLASS INSIGHT")
    print("-" * 70)

    if percentages:

        if class_average >= 90:

            print(
                "The class is performing at an "
                "excellent academic level."
            )

        elif class_average >= 70:

            print(
                "The class is performing at a "
                "good academic level."
            )

        elif class_average >= 50:

            print(
                "The class has an average level "
                "of academic performance."
            )

        else:

            print(
                "The class requires significant "
                "academic improvement."
            )

        if categories["Excellent"] > 0:

            print(
                f"{categories['Excellent']} student(s) "
                "are currently in the Excellent category."
            )

        if categories["Needs Attention"] > 0:

            print(
                f"{categories['Needs Attention']} student(s) "
                "need additional academic attention."
            )

    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    print("\nCLASS RECOMMENDATIONS")
    print("-" * 70)

    recommendations = generate_class_recommendations(
        class_average,
        categories,
        weakest_subject,
        study_statistics
    )

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        print(
            f"{index}. {recommendation}"
        )

    # ========================================================
    # FOOTER
    # ========================================================

    print("\n" + "=" * 70)
    print(
        "             END OF CLASS DASHBOARD"
    )
    print("=" * 70)


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

def main():
    """Run the class performance dashboard."""

    display_class_dashboard()


if __name__ == "__main__":
    main()

