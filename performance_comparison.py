import csv
import os


# ============================================================
# FILE PATHS
# ============================================================

STUDENTS_FILE = "data/students.csv"
SUBJECT_MARKS_FILE = "data/subject_marks.csv"
STUDY_HOURS_FILE = "data/study_hours.csv"


# ============================================================
# LOAD STUDENT DATA
# ============================================================

def load_students():
    """Load student performance data from CSV."""

    if not os.path.exists(STUDENTS_FILE):
        return []

    try:

        with open(
            STUDENTS_FILE,
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


# ============================================================
# LOAD SUBJECT DATA
# ============================================================

def load_subject_marks():
    """Load subject-wise marks from CSV."""

    if not os.path.exists(SUBJECT_MARKS_FILE):
        return []

    try:

        with open(
            SUBJECT_MARKS_FILE,
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


# ============================================================
# LOAD STUDY HOURS
# ============================================================

def load_study_hours():
    """Load student study-hour records."""

    if not os.path.exists(STUDY_HOURS_FILE):
        return []

    try:

        with open(
            STUDY_HOURS_FILE,
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


# ============================================================
# FIND STUDENT
# ============================================================

def find_student(students, name):
    """Find a student by name."""

    for student in students:

        if (
            student["Name"].strip().lower()
            == name.strip().lower()
        ):

            return student

    return None


# ============================================================
# GET SUBJECT MARKS
# ============================================================

def get_student_subjects(
    subject_data,
    student_name
):
    """Get subject marks for a particular student."""

    subjects = {}

    for row in subject_data:

        if (
            row["Name"].strip().lower()
            == student_name.strip().lower()
        ):

            try:

                subjects[row["Subject"]] = float(
                    row["Marks"]
                )

            except (
                ValueError,
                KeyError
            ):

                continue

    return subjects


# ============================================================
# GET STUDY HOURS
# ============================================================

def get_student_study_hours(
    study_data,
    student_name
):
    """Get study hours for a particular student."""

    for row in study_data:

        if (
            row["Name"].strip().lower()
            == student_name.strip().lower()
        ):

            try:

                return float(
                    row["StudyHours"]
                )

            except (
                ValueError,
                KeyError
            ):

                return None

    return None


# ============================================================
# CALCULATE TOTAL MARKS
# ============================================================

def calculate_total_marks(subjects):
    """Calculate total marks from subject marks."""

    return sum(
        subjects.values()
    )


# ============================================================
# GET PERFORMANCE CATEGORY
# ============================================================

def get_performance_category(
    percentage
):
    """Return the performance category."""

    if percentage >= 90:

        return "Excellent"

    elif percentage >= 70:

        return "Good"

    elif percentage >= 50:

        return "Average"

    else:

        return "Needs Attention"


# ============================================================
# DISPLAY STUDENT SUMMARY
# ============================================================

def display_student_summary(
    student,
    subjects,
    study_hours
):
    """Display a compact summary for a student."""

    percentage = float(
        student["Percentage"]
    )

    total = calculate_total_marks(
        subjects
    )

    category = get_performance_category(
        percentage
    )

    print(
        f"\nStudent             : {student['Name']}"
    )

    print(
        f"Total Marks         : {total:.2f}"
    )

    print(
        f"Percentage          : {percentage:.2f}%"
    )

    print(
        f"Grade               : {student['Grade']}"
    )

    print(
        f"Performance Category: {category}"
    )

    if study_hours is not None:

        print(
            f"Study Hours         : "
            f"{study_hours:.2f} hours/day"
        )

    else:

        print(
            "Study Hours         : Data unavailable"
        )


# ============================================================
# COMPARE STUDENTS
# ============================================================

def compare_students():
    """Compare the academic performance of two students."""

    students = load_students()

    if not students:

        print(
            "\nNo student data available."
        )

        return

    print(
        "\n" + "=" * 70
    )

    print(
        "                    STUDENT COMPARISON"
    )

    print(
        "=" * 70
    )

    # --------------------------------------------------------
    # Student Selection
    # --------------------------------------------------------

    name1 = input(
        "\nEnter first student name: "
    ).strip()

    name2 = input(
        "Enter second student name: "
    ).strip()

    student1 = find_student(
        students,
        name1
    )

    student2 = find_student(
        students,
        name2
    )

    if not student1:

        print(
            f"\nStudent '{name1}' was not found."
        )

        return

    if not student2:

        print(
            f"\nStudent '{name2}' was not found."
        )

        return

    if (
        student1["Name"].strip().lower()
        == student2["Name"].strip().lower()
    ):

        print(
            "\nPlease select two different students."
        )

        return

    # --------------------------------------------------------
    # Academic Data
    # --------------------------------------------------------

    percentage1 = float(
        student1["Percentage"]
    )

    percentage2 = float(
        student2["Percentage"]
    )

    # --------------------------------------------------------
    # Subject Data
    # --------------------------------------------------------

    subject_data = load_subject_marks()

    subjects1 = get_student_subjects(
        subject_data,
        student1["Name"]
    )

    subjects2 = get_student_subjects(
        subject_data,
        student2["Name"]
    )

    total1 = calculate_total_marks(
        subjects1
    )

    total2 = calculate_total_marks(
        subjects2
    )

    # --------------------------------------------------------
    # Study Data
    # --------------------------------------------------------

    study_data = load_study_hours()

    study_hours1 = get_student_study_hours(
        study_data,
        student1["Name"]
    )

    study_hours2 = get_student_study_hours(
        study_data,
        student2["Name"]
    )

    # ========================================================
    # ACADEMIC PERFORMANCE
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "ACADEMIC PERFORMANCE"
    )

    print(
        "-" * 70
    )

    print(
        f"{'':22}"
        f"{student1['Name']:<22}"
        f"{student2['Name']:<22}"
    )

    print(
        f"{'Total Marks':22}"
        f"{total1:<22.2f}"
        f"{total2:<22.2f}"
    )

    print(
        f"{'Percentage':22}"
        f"{percentage1:<22.2f}"
        f"{percentage2:<22.2f}"
    )

    print(
        f"{'Grade':22}"
        f"{student1['Grade']:<22}"
        f"{student2['Grade']:<22}"
    )

    print(
        f"{'Category':22}"
        f"{get_performance_category(percentage1):<22}"
        f"{get_performance_category(percentage2):<22}"
    )

    # ========================================================
    # STUDY HABITS COMPARISON
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "LEARNING HABITS COMPARISON"
    )

    print(
        "-" * 70
    )

    print(
        f"{'':22}"
        f"{student1['Name']:<22}"
        f"{student2['Name']:<22}"
    )

    if study_hours1 is not None:

        study1_display = (
            f"{study_hours1:.2f} hrs/day"
        )

    else:

        study1_display = "Not available"

    if study_hours2 is not None:

        study2_display = (
            f"{study_hours2:.2f} hrs/day"
        )

    else:

        study2_display = "Not available"

    print(
        f"{'Study Hours':22}"
        f"{study1_display:<22}"
        f"{study2_display:<22}"
    )

    # --------------------------------------------------------
    # Study Hours Result
    # --------------------------------------------------------

    if (
        study_hours1 is not None
        and study_hours2 is not None
    ):

        study_difference = abs(
            study_hours1 - study_hours2
        )

        print(
            f"\nStudy Time Difference : "
            f"{study_difference:.2f} hours/day"
        )

        if study_hours1 > study_hours2:

            print(
                f"More Study Time      : "
                f"{student1['Name']}"
            )

        elif study_hours2 > study_hours1:

            print(
                f"More Study Time      : "
                f"{student2['Name']}"
            )

        else:

            print(
                "Study Time Result    : "
                "Both students study for the same average time."
            )

    else:

        print(
            "\nStudy-time comparison requires "
            "study data for both students."
        )

    # ========================================================
    # OVERALL COMPARISON
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "OVERALL COMPARISON RESULT"
    )

    print(
        "-" * 70
    )

    difference = abs(
        percentage1 - percentage2
    )

    if percentage1 > percentage2:

        higher_student = student1
        lower_student = student2

        print(
            f"Higher Performer : "
            f"{student1['Name']}"
        )

    elif percentage2 > percentage1:

        higher_student = student2
        lower_student = student1

        print(
            f"Higher Performer : "
            f"{student2['Name']}"
        )

    else:

        higher_student = None
        lower_student = None

        print(
            "Result            : "
            "Both students have equal performance."
        )

    print(
        f"Score Difference  : "
        f"{difference:.2f} percentage points"
    )

    # ========================================================
    # SUBJECT-WISE COMPARISON
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "SUBJECT-WISE COMPARISON"
    )

    print(
        "-" * 70
    )

    common_subjects = sorted(
        set(subjects1.keys())
        &
        set(subjects2.keys())
    )

    if common_subjects:

        print(
            f"{'Subject':22}"
            f"{student1['Name']:<22}"
            f"{student2['Name']:<22}"
        )

        print(
            "-" * 70
        )

        for subject in common_subjects:

            mark1 = subjects1[subject]
            mark2 = subjects2[subject]

            print(
                f"{subject:<22}"
                f"{mark1:<22.2f}"
                f"{mark2:<22.2f}"
            )

    else:

        print(
            "No common subject data available."
        )

    # ========================================================
    # SUBJECT WINNERS
    # ========================================================

    if common_subjects:

        print(
            "\n" + "-" * 70
        )

        print(
            "SUBJECT WINNERS"
        )

        print(
            "-" * 70
        )

        student1_subject_wins = 0
        student2_subject_wins = 0
        equal_subjects = 0

        for subject in common_subjects:

            mark1 = subjects1[subject]
            mark2 = subjects2[subject]

            if mark1 > mark2:

                student1_subject_wins += 1

                print(
                    f"{subject:<18}: "
                    f"{student1['Name']} "
                    f"(+{mark1 - mark2:.2f})"
                )

            elif mark2 > mark1:

                student2_subject_wins += 1

                print(
                    f"{subject:<18}: "
                    f"{student2['Name']} "
                    f"(+{mark2 - mark1:.2f})"
                )

            else:

                equal_subjects += 1

                print(
                    f"{subject:<18}: "
                    f"Equal performance"
                )

        print(
            "\nSubject Wins Summary"
        )

        print(
            f"{student1['Name']:<22}: "
            f"{student1_subject_wins}"
        )

        print(
            f"{student2['Name']:<22}: "
            f"{student2_subject_wins}"
        )

        print(
            f"{'Equal':<22}: "
            f"{equal_subjects}"
        )

    # ========================================================
    # SUBJECT INSIGHTS
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "SUBJECT INSIGHTS"
    )

    print(
        "-" * 70
    )

    if subjects1:

        strongest1 = max(
            subjects1,
            key=subjects1.get
        )

        weakest1 = min(
            subjects1,
            key=subjects1.get
        )

        print(
            f"{student1['Name']} strongest : "
            f"{strongest1} "
            f"({subjects1[strongest1]:.2f}%)"
        )

        print(
            f"{student1['Name']} weakest   : "
            f"{weakest1} "
            f"({subjects1[weakest1]:.2f}%)"
        )

    else:

        print(
            f"No subject data available for "
            f"{student1['Name']}."
        )

    if subjects2:

        strongest2 = max(
            subjects2,
            key=subjects2.get
        )

        weakest2 = min(
            subjects2,
            key=subjects2.get
        )

        print(
            f"{student2['Name']} strongest : "
            f"{strongest2} "
            f"({subjects2[strongest2]:.2f}%)"
        )

        print(
            f"{student2['Name']} weakest   : "
            f"{weakest2} "
            f"({subjects2[weakest2]:.2f}%)"
        )

    else:

        print(
            f"No subject data available for "
            f"{student2['Name']}."
        )

    # ========================================================
    # PERFORMANCE GAP ANALYSIS
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "PERFORMANCE GAP ANALYSIS"
    )

    print(
        "-" * 70
    )

    if difference == 0:

        print(
            "There is no overall performance gap "
            "between the two students."
        )

    elif difference < 5:

        print(
            "The performance gap is small. "
            "Both students are performing at a similar level."
        )

    elif difference < 15:

        print(
            "There is a moderate performance gap "
            "between the students."
        )

    else:

        print(
            "There is a significant performance gap "
            "between the students."
        )

    # ========================================================
    # STUDY VS PERFORMANCE INSIGHT
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "STUDY VS PERFORMANCE INSIGHT"
    )

    print(
        "-" * 70
    )

    if (
        study_hours1 is not None
        and study_hours2 is not None
    ):

        if (
            study_hours1 > study_hours2
            and percentage1 > percentage2
        ):

            print(
                f"{student1['Name']} studies more and "
                f"currently has the higher percentage."
            )

        elif (
            study_hours2 > study_hours1
            and percentage2 > percentage1
        ):

            print(
                f"{student2['Name']} studies more and "
                f"currently has the higher percentage."
            )

        elif (
            study_hours1 > study_hours2
            and percentage1 < percentage2
        ):

            print(
                f"{student2['Name']} has a higher percentage "
                f"despite studying fewer hours."
            )

        elif (
            study_hours2 > study_hours1
            and percentage2 < percentage1
        ):

            print(
                f"{student1['Name']} has a higher percentage "
                f"despite studying fewer hours."
            )

        else:

            print(
                "Study time and academic performance "
                "show a mixed pattern in this comparison."
            )

        print(
            "Note: This comparison describes the current "
            "student data and does not establish causation."
        )

    else:

        print(
            "Study-performance insight cannot be calculated "
            "because study data is incomplete."
        )

    # ========================================================
    # FINAL COMPARISON INSIGHT
    # ========================================================

    print(
        "\n" + "-" * 70
    )

    print(
        "PERSONALIZED COMPARISON INSIGHT"
    )

    print(
        "-" * 70
    )

    if higher_student:

        print(
            f"{higher_student['Name']} is currently ahead "
            f"by {difference:.2f} percentage points."
        )

        print(
            f"{lower_student['Name']} can focus on "
            "improving weaker subjects and maintaining "
            "regular practice."
        )

    else:

        print(
            "Both students have the same overall percentage."
        )

        print(
            "Both students should continue strengthening "
            "their weaker subjects."
        )

    # --------------------------------------------------------
    # Strongest Subject Comparison
    # --------------------------------------------------------

    if common_subjects:

        best_gap_subject = max(
            common_subjects,
            key=lambda subject:
            abs(
                subjects1[subject]
                -
                subjects2[subject]
            )
        )

        gap = abs(
            subjects1[best_gap_subject]
            -
            subjects2[best_gap_subject]
        )

        if gap > 0:

            if (
                subjects1[best_gap_subject]
                >
                subjects2[best_gap_subject]
            ):

                print(
                    f"\nLargest subject gap: "
                    f"{best_gap_subject} — "
                    f"{student1['Name']} leads by "
                    f"{gap:.2f} marks."
                )

            else:

                print(
                    f"\nLargest subject gap: "
                    f"{best_gap_subject} — "
                    f"{student2['Name']} leads by "
                    f"{gap:.2f} marks."
                )

    print(
        "\n" + "=" * 70
    )

    print(
        "Comparison completed successfully."
    )

    print(
        "=" * 70
    )