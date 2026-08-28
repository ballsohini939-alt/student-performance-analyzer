
import csv
import os


STUDENTS_FILE = "data/students.csv"
SUBJECT_MARKS_FILE = "data/subject_marks.csv"
STUDY_HOURS_FILE = "data/study_hours.csv"
REPORTS_FOLDER = "reports"


# ============================================================
# LOAD DATA
# ============================================================

def load_students():
    """Load student academic records."""

    if not os.path.exists(STUDENTS_FILE):
        return []

    with open(
        STUDENTS_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        return list(csv.DictReader(file))


def load_subject_marks():
    """Load subject-wise marks."""

    if not os.path.exists(SUBJECT_MARKS_FILE):
        return []

    with open(
        SUBJECT_MARKS_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        return list(csv.DictReader(file))


def load_study_hours():
    """Load study-hour records."""

    if not os.path.exists(STUDY_HOURS_FILE):
        return []

    with open(
        STUDY_HOURS_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        return list(csv.DictReader(file))


# ============================================================
# STUDENT DATA
# ============================================================

def get_student_data(name):
    """Collect all available information for a student."""

    students = load_students()
    subject_marks = load_subject_marks()
    study_hours = load_study_hours()

    student = None

    for record in students:
        if (
            record["Name"].strip().lower()
            == name.strip().lower()
        ):
            student = record
            break

    if student is None:
        return None

    subjects = []

    for record in subject_marks:
        if (
            record["Name"].strip().lower()
            == name.strip().lower()
        ):
            subjects.append(
                {
                    "subject": record["Subject"],
                    "marks": float(record["Marks"])
                }
            )

    study = None

    for record in study_hours:
        if (
            record["Name"].strip().lower()
            == name.strip().lower()
        ):
            study = float(record["StudyHours"])
            break

    percentage = float(student["Percentage"])

    if percentage >= 90:
        recommendation = (
            "Excellent performance. Maintain your current "
            "study routine and continue challenging yourself."
        )

    elif percentage >= 70:
        recommendation = (
            "Good performance. Continue practicing regularly "
            "and focus on reaching the excellent category."
        )

    elif percentage >= 50:
        recommendation = (
            "Average performance. Focus on weak subjects, "
            "practice regularly, and increase study consistency."
        )

    else:
        recommendation = (
            "Needs significant improvement. Focus on weak "
            "subjects and follow a consistent study schedule."
        )

    return {
        "name": student["Name"],
        "total": float(student["Total"]),
        "percentage": percentage,
        "grade": student["Grade"],
        "subjects": subjects,
        "study_hours": study,
        "recommendation": recommendation
    }


# ============================================================
# STUDENT REPORT
# ============================================================

def generate_student_report(name):
    """Generate and save a text report for a student."""

    data = get_student_data(name)

    if data is None:
        return None

    os.makedirs(
        REPORTS_FOLDER,
        exist_ok=True
    )

    safe_name = "".join(
        character
        if character.isalnum() or character in "_-"
        else "_"
        for character in data["name"]
    )

    report_path = os.path.join(
        REPORTS_FOLDER,
        f"{safe_name}_report.txt"
    )

    report = []

    report.append("=" * 60)
    report.append(
        "           STUDENT PERFORMANCE REPORT"
    )
    report.append("=" * 60)

    report.append("")
    report.append("STUDENT INFORMATION")
    report.append("-" * 60)

    report.append(
        f"Name       : {data['name']}"
    )

    report.append(
        f"Total Marks: {data['total']:.2f}"
    )

    report.append(
        f"Percentage  : {data['percentage']:.2f}%"
    )

    report.append(
        f"Grade       : {data['grade']}"
    )

    report.append("")
    report.append("SUBJECT PERFORMANCE")
    report.append("-" * 60)

    if data["subjects"]:

        for subject in data["subjects"]:

            report.append(
                f"{subject['subject']:<20} "
                f"{subject['marks']:.2f}"
            )

    else:

        report.append(
            "No subject-wise data available."
        )

    report.append("")
    report.append("LEARNING HABITS")
    report.append("-" * 60)

    if data["study_hours"] is not None:

        report.append(
            f"Average Study Hours : "
            f"{data['study_hours']:.2f} hours/day"
        )

    else:

        report.append(
            "Study hours data not available."
        )

    report.append("")
    report.append("PERSONALIZED RECOMMENDATION")
    report.append("-" * 60)

    report.append(
        data["recommendation"]
    )

    report.append("")
    report.append("=" * 60)
    report.append(
        "Generated by Student Performance Analyzer"
    )
    report.append("=" * 60)

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "\n".join(report)
        )

    return report_path


# ============================================================
# CLASS REPORT
# ============================================================

def generate_class_report():
    """
    Generate and save a complete class performance report.

    Includes:
    - Class overview
    - Top performer
    - Lowest performer
    - Grade distribution
    - Performance categories
    - Subject performance
    - Learning habits
    - Students needing attention
    - Class insights
    - Recommendations
    """

    students = load_students()
    subject_marks = load_subject_marks()
    study_hours = load_study_hours()

    if not students:
        return None

    os.makedirs(
        REPORTS_FOLDER,
        exist_ok=True
    )

    # --------------------------------------------------------
    # CLASS STATISTICS
    # --------------------------------------------------------

    percentages = [
        float(student["Percentage"])
        for student in students
    ]

    total_students = len(students)

    class_average = (
        sum(percentages)
        / total_students
    )

    highest_student = max(
        students,
        key=lambda student:
        float(student["Percentage"])
    )

    lowest_student = min(
        students,
        key=lambda student:
        float(student["Percentage"])
    )

    # --------------------------------------------------------
    # GRADE DISTRIBUTION
    # --------------------------------------------------------

    grade_distribution = {}

    for student in students:

        grade = student["Grade"]

        grade_distribution[grade] = (
            grade_distribution.get(
                grade,
                0
            ) + 1
        )

    # --------------------------------------------------------
    # PERFORMANCE CATEGORIES
    # --------------------------------------------------------

    categories = {
        "Excellent": 0,
        "Good": 0,
        "Average": 0,
        "Needs Attention": 0
    }

    for percentage in percentages:

        if percentage >= 90:

            categories["Excellent"] += 1

        elif percentage >= 70:

            categories["Good"] += 1

        elif percentage >= 50:

            categories["Average"] += 1

        else:

            categories["Needs Attention"] += 1

    # --------------------------------------------------------
    # SUBJECT STATISTICS
    # --------------------------------------------------------

    subject_data = {}

    for record in subject_marks:

        subject = record["Subject"]
        marks = float(record["Marks"])

        if subject not in subject_data:

            subject_data[subject] = []

        subject_data[subject].append(
            marks
        )

    subject_averages = {}

    for subject, marks in subject_data.items():

        subject_averages[subject] = (
            sum(marks)
            / len(marks)
        )

    strongest_subject = None
    weakest_subject = None

    if subject_averages:

        strongest_subject = max(
            subject_averages,
            key=subject_averages.get
        )

        weakest_subject = min(
            subject_averages,
            key=subject_averages.get
        )

    # --------------------------------------------------------
    # STUDY STATISTICS
    # --------------------------------------------------------

    study_values = []

    for record in study_hours:

        try:

            study_values.append(
                (
                    record["Name"],
                    float(record["StudyHours"])
                )
            )

        except (
            KeyError,
            ValueError
        ):

            continue

    average_study_hours = None
    highest_study = None
    lowest_study = None

    if study_values:

        hours = [
            value
            for name, value in study_values
        ]

        average_study_hours = (
            sum(hours)
            / len(hours)
        )

        highest_study = max(
            study_values,
            key=lambda item: item[1]
        )

        lowest_study = min(
            study_values,
            key=lambda item: item[1]
        )

    # --------------------------------------------------------
    # BUILD REPORT
    # --------------------------------------------------------

    report = []

    report.append("=" * 70)
    report.append(
        "             CLASS PERFORMANCE REPORT"
    )
    report.append("=" * 70)

    # --------------------------------------------------------
    # CLASS OVERVIEW
    # --------------------------------------------------------

    report.append("")
    report.append("CLASS OVERVIEW")
    report.append("-" * 70)

    report.append(
        f"Total Students       : {total_students}"
    )

    report.append(
        f"Class Average        : "
        f"{class_average:.2f}%"
    )

    report.append(
        f"Highest Percentage   : "
        f"{float(highest_student['Percentage']):.2f}%"
    )

    report.append(
        f"Lowest Percentage    : "
        f"{float(lowest_student['Percentage']):.2f}%"
    )

    # --------------------------------------------------------
    # TOP PERFORMER
    # --------------------------------------------------------

    report.append("")
    report.append("TOP PERFORMER")
    report.append("-" * 70)

    report.append(
        f"Name                 : "
        f"{highest_student['Name']}"
    )

    report.append(
        f"Percentage           : "
        f"{float(highest_student['Percentage']):.2f}%"
    )

    report.append(
        f"Grade                : "
        f"{highest_student['Grade']}"
    )

    # --------------------------------------------------------
    # STUDENT NEEDING MOST ATTENTION
    # --------------------------------------------------------

    report.append("")
    report.append(
        "STUDENT NEEDING MOST ATTENTION"
    )
    report.append("-" * 70)

    report.append(
        f"Name                 : "
        f"{lowest_student['Name']}"
    )

    report.append(
        f"Percentage           : "
        f"{float(lowest_student['Percentage']):.2f}%"
    )

    report.append(
        f"Grade                : "
        f"{lowest_student['Grade']}"
    )

    # --------------------------------------------------------
    # GRADE DISTRIBUTION
    # --------------------------------------------------------

    report.append("")
    report.append("GRADE DISTRIBUTION")
    report.append("-" * 70)

    for grade, count in grade_distribution.items():

        report.append(
            f"{grade:<20}: "
            f"{count} student(s)"
        )

    # --------------------------------------------------------
    # PERFORMANCE CATEGORIES
    # --------------------------------------------------------

    report.append("")
    report.append("PERFORMANCE CATEGORIES")
    report.append("-" * 70)

    for category, count in categories.items():

        report.append(
            f"{category:<20}: "
            f"{count} student(s)"
        )

    # --------------------------------------------------------
    # SUBJECT PERFORMANCE
    # --------------------------------------------------------

    report.append("")
    report.append("SUBJECT PERFORMANCE")
    report.append("-" * 70)

    if subject_averages:

        for subject in sorted(
            subject_averages
        ):

            report.append(
                f"{subject:<20}: "
                f"{subject_averages[subject]:.2f}%"
            )

        report.append("")

        report.append(
            f"Strongest Subject    : "
            f"{strongest_subject} "
            f"({subject_averages[strongest_subject]:.2f}%)"
        )

        report.append(
            f"Weakest Subject      : "
            f"{weakest_subject} "
            f"({subject_averages[weakest_subject]:.2f}%)"
        )

    else:

        report.append(
            "No subject-wise data available."
        )

    # --------------------------------------------------------
    # LEARNING HABITS
    # --------------------------------------------------------

    report.append("")
    report.append("LEARNING HABITS")
    report.append("-" * 70)

    if average_study_hours is not None:

        report.append(
            f"Average Study Hours  : "
            f"{average_study_hours:.2f} hours/day"
        )

        report.append(
            f"Highest Study Hours  : "
            f"{highest_study[0]} "
            f"({highest_study[1]:.2f} hours/day)"
        )

        report.append(
            f"Lowest Study Hours   : "
            f"{lowest_study[0]} "
            f"({lowest_study[1]:.2f} hours/day)"
        )

    else:

        report.append(
            "No study-hour data available."
        )

    # --------------------------------------------------------
    # STUDENTS NEEDING ATTENTION
    # --------------------------------------------------------

    report.append("")
    report.append(
        "STUDENTS NEEDING ACADEMIC ATTENTION"
    )
    report.append("-" * 70)

    attention_students = [
        student
        for student in students
        if float(student["Percentage"]) < 50
    ]

    if attention_students:

        for student in attention_students:

            report.append(
                f"{student['Name']:<20} "
                f"{float(student['Percentage']):.2f}% "
                f"Grade: {student['Grade']}"
            )

    else:

        report.append(
            "No students currently require "
            "significant academic attention."
        )

    # --------------------------------------------------------
    # CLASS INSIGHT
    # --------------------------------------------------------

    report.append("")
    report.append("CLASS INSIGHT")
    report.append("-" * 70)

    if class_average >= 85:

        report.append(
            "The class is performing at an "
            "excellent level."
        )

    elif class_average >= 70:

        report.append(
            "The class is performing at a "
            "good level."
        )

    elif class_average >= 50:

        report.append(
            "The class has an average level "
            "of academic performance."
        )

    else:

        report.append(
            "The class requires significant "
            "academic improvement."
        )

    report.append(
        f"{categories['Excellent']} student(s) "
        "are currently in the Excellent category."
    )

    report.append(
        f"{categories['Needs Attention']} student(s) "
        "need additional academic attention."
    )

    # --------------------------------------------------------
    # CLASS RECOMMENDATIONS
    # --------------------------------------------------------

    report.append("")
    report.append("CLASS RECOMMENDATIONS")
    report.append("-" * 70)

    if categories["Needs Attention"] > 0:

        report.append(
            "- Provide additional support to "
            "students performing below 50%."
        )

    if weakest_subject:

        report.append(
            "- Give additional practice and "
            f"support in {weakest_subject}."
        )

    if average_study_hours is not None:

        report.append(
            "- Encourage students to maintain "
            "a consistent study routine."
        )

    if categories["Excellent"] > 0:

        report.append(
            "- Encourage high-performing students "
            "with advanced practice."
        )

    # --------------------------------------------------------
    # REPORT FOOTER
    # --------------------------------------------------------

    report.append("")
    report.append("=" * 70)
    report.append(
        "Generated by Student Performance Analyzer"
    )
    report.append("=" * 70)

    # --------------------------------------------------------
    # SAVE REPORT
    # --------------------------------------------------------

    report_path = os.path.join(
        REPORTS_FOLDER,
        "class_performance_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "\n".join(report)
        )

    return report_path

